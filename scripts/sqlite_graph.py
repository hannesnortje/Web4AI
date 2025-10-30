#!/usr/bin/env python3
"""
SQLite-based Graph Storage for PDCA Relationships
Alternative to RedisGraph for three-tier RAG system

This module provides graph functionality for storing and querying
PDCA relationships using SQLite as the graph database tier.
"""

import sqlite3
import json
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SQLiteGraph:
    """
    SQLite-based graph storage for PDCA relationships.
    
    Provides graph functionality including:
    - Node creation and management
    - Edge creation and traversal
    - Breadcrumb navigation
    - Graph queries and analytics
    """
    
    def __init__(self, db_path: str = "pdca_timeline.db"):
        """Initialize SQLite graph database."""
        self.db_path = db_path
        self.conn = None
        self._init_database()
    
    def _init_database(self):
        """Initialize database schema for graph operations."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Enable column access by name
        
        # Create tables if they don't exist
        self._create_schema()
        logger.info(f"SQLite graph database initialized at {self.db_path}")
    
    def _create_schema(self):
        """Create database schema for graph operations."""
        cursor = self.conn.cursor()
        
        # PDCA nodes table (if not exists)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pdcas (
                id TEXT PRIMARY KEY,
                agent_name TEXT NOT NULL,
                agent_role TEXT NOT NULL,
                date TEXT NOT NULL,
                timestamp INTEGER NOT NULL,
                session_id TEXT,
                branch TEXT,
                sprint TEXT,
                cmm_level INTEGER,
                task_type TEXT,
                objective TEXT,
                quality_score REAL,
                verification_status TEXT,
                file_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Graph relationships table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pdca_relationships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_pdca_id TEXT NOT NULL,
                to_pdca_id TEXT NOT NULL,
                relationship_type TEXT DEFAULT 'PRECEDES',
                weight REAL DEFAULT 1.0,
                metadata TEXT,  -- JSON metadata for additional properties
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (from_pdca_id) REFERENCES pdcas(id),
                FOREIGN KEY (to_pdca_id) REFERENCES pdcas(id),
                UNIQUE(from_pdca_id, to_pdca_id, relationship_type)
            )
        """)
        
        # Create indexes for fast graph traversal
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_pdca_relationships_from 
            ON pdca_relationships(from_pdca_id)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_pdca_relationships_to 
            ON pdca_relationships(to_pdca_id)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_pdca_relationships_type 
            ON pdca_relationships(relationship_type)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_pdcas_date 
            ON pdcas(date)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_pdcas_agent 
            ON pdcas(agent_name)
        """)
        
        self.conn.commit()
        logger.info("Database schema created/verified")
    
    def add_pdca_node(self, pdca_data: Dict) -> bool:
        """
        Add a PDCA node to the graph.
        
        Args:
            pdca_data: Dictionary containing PDCA information
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            
            # Insert or update PDCA node
            cursor.execute("""
                INSERT OR REPLACE INTO pdcas (
                    id, agent_name, agent_role, date, timestamp,
                    session_id, branch, sprint, cmm_level, task_type,
                    objective, quality_score, verification_status, file_path
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                pdca_data.get('id'),
                pdca_data.get('agent_name'),
                pdca_data.get('agent_role'),
                pdca_data.get('date'),
                pdca_data.get('timestamp'),
                pdca_data.get('session_id', ''),
                pdca_data.get('branch', ''),
                pdca_data.get('sprint', ''),
                pdca_data.get('cmm_level', 0),
                pdca_data.get('task_type', ''),
                pdca_data.get('objective', ''),
                pdca_data.get('quality_score', 0.0),
                pdca_data.get('verification_status', ''),
                pdca_data.get('file_path', '')
            ))
            
            self.conn.commit()
            logger.debug(f"Added PDCA node: {pdca_data.get('id')}")
            return True
            
        except Exception as e:
            logger.error(f"Error adding PDCA node: {e}")
            return False
    
    def add_relationship(self, from_pdca_id: str, to_pdca_id: str, 
                        relationship_type: str = "PRECEDES", 
                        weight: float = 1.0, metadata: Dict = None) -> bool:
        """
        Add a relationship between two PDCAs.
        
        Args:
            from_pdca_id: Source PDCA ID
            to_pdca_id: Target PDCA ID
            relationship_type: Type of relationship (default: PRECEDES)
            weight: Relationship weight (default: 1.0)
            metadata: Additional metadata as dictionary
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            
            metadata_json = json.dumps(metadata) if metadata else None
            
            cursor.execute("""
                INSERT OR REPLACE INTO pdca_relationships (
                    from_pdca_id, to_pdca_id, relationship_type, weight, metadata
                ) VALUES (?, ?, ?, ?, ?)
            """, (from_pdca_id, to_pdca_id, relationship_type, weight, metadata_json))
            
            self.conn.commit()
            logger.debug(f"Added relationship: {from_pdca_id} -> {to_pdca_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error adding relationship: {e}")
            return False
    
    def get_predecessors(self, pdca_id: str, relationship_type: str = "PRECEDES") -> List[Dict]:
        """
        Get all PDCAs that precede the given PDCA.
        
        Args:
            pdca_id: Target PDCA ID
            relationship_type: Type of relationship to follow
            
        Returns:
            List of predecessor PDCAs with metadata
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT p.*, pr.weight, pr.metadata, pr.created_at as relationship_created
                FROM pdcas p
                JOIN pdca_relationships pr ON p.id = pr.from_pdca_id
                WHERE pr.to_pdca_id = ? AND pr.relationship_type = ?
                ORDER BY pr.created_at DESC
            """, (pdca_id, relationship_type))
            
            results = []
            for row in cursor.fetchall():
                pdca_dict = dict(row)
                if pdca_dict['metadata']:
                    pdca_dict['metadata'] = json.loads(pdca_dict['metadata'])
                results.append(pdca_dict)
            
            logger.debug(f"Found {len(results)} predecessors for {pdca_id}")
            return results
            
        except Exception as e:
            logger.error(f"Error getting predecessors: {e}")
            return []
    
    def get_successors(self, pdca_id: str, relationship_type: str = "PRECEDES") -> List[Dict]:
        """
        Get all PDCAs that follow the given PDCA.
        
        Args:
            pdca_id: Source PDCA ID
            relationship_type: Type of relationship to follow
            
        Returns:
            List of successor PDCAs with metadata
        """
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                SELECT p.*, pr.weight, pr.metadata, pr.created_at as relationship_created
                FROM pdcas p
                JOIN pdca_relationships pr ON p.id = pr.to_pdca_id
                WHERE pr.from_pdca_id = ? AND pr.relationship_type = ?
                ORDER BY pr.created_at DESC
            """, (pdca_id, relationship_type))
            
            results = []
            for row in cursor.fetchall():
                pdca_dict = dict(row)
                if pdca_dict['metadata']:
                    pdca_dict['metadata'] = json.loads(pdca_dict['metadata'])
                results.append(pdca_dict)
            
            logger.debug(f"Found {len(results)} successors for {pdca_id}")
            return results
            
        except Exception as e:
            logger.error(f"Error getting successors: {e}")
            return []
    
    def find_path(self, start_pdca_id: str, end_pdca_id: str, 
                  relationship_type: str = "PRECEDES", max_depth: int = 10) -> List[Dict]:
        """
        Find a path between two PDCAs using recursive SQL.
        
        Args:
            start_pdca_id: Starting PDCA ID
            end_pdca_id: Target PDCA ID
            relationship_type: Type of relationship to follow
            max_depth: Maximum search depth
            
        Returns:
            List of PDCAs forming the path, or empty list if no path found
        """
        try:
            cursor = self.conn.cursor()
            
            # Use recursive CTE to find path
            cursor.execute("""
                WITH RECURSIVE pdca_path AS (
                    -- Base case: start node
                    SELECT p.*, 0 as depth, CAST(p.id AS TEXT) as path
                    FROM pdcas p
                    WHERE p.id = ?
                    
                    UNION ALL
                    
                    -- Recursive case: follow relationships
                    SELECT p.*, pp.depth + 1, pp.path || ' -> ' || p.id
                    FROM pdcas p
                    JOIN pdca_relationships pr ON p.id = pr.to_pdca_id
                    JOIN pdca_path pp ON pr.from_pdca_id = pp.id
                    WHERE pp.depth < ? AND pr.relationship_type = ?
                )
                SELECT * FROM pdca_path 
                WHERE id = ? OR depth = ?
                ORDER BY depth
            """, (start_pdca_id, max_depth, relationship_type, end_pdca_id, max_depth))
            
            results = []
            for row in cursor.fetchall():
                results.append(dict(row))
            
            logger.debug(f"Found path of length {len(results)} from {start_pdca_id} to {end_pdca_id}")
            return results
            
        except Exception as e:
            logger.error(f"Error finding path: {e}")
            return []
    
    def get_breadcrumb_navigation(self, pdca_id: str, max_depth: int = 5) -> Dict:
        """
        Get breadcrumb navigation for a PDCA (predecessors and successors).
        
        Args:
            pdca_id: PDCA ID to get navigation for
            max_depth: Maximum depth to search
            
        Returns:
            Dictionary with predecessors, successors, and path information
        """
        try:
            predecessors = self.get_predecessors(pdca_id)
            successors = self.get_successors(pdca_id)
            
            # Get current PDCA info
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM pdcas WHERE id = ?", (pdca_id,))
            row = cursor.fetchone()
            current_pdca = dict(row) if row else None
            
            return {
                'current_pdca': current_pdca,
                'predecessors': predecessors[:max_depth],
                'successors': successors[:max_depth],
                'predecessor_count': len(predecessors),
                'successor_count': len(successors)
            }
            
        except Exception as e:
            logger.error(f"Error getting breadcrumb navigation: {e}")
            return {}
    
    def get_graph_stats(self) -> Dict:
        """
        Get graph statistics and analytics.
        
        Returns:
            Dictionary with graph statistics
        """
        try:
            cursor = self.conn.cursor()
            
            # Node count
            cursor.execute("SELECT COUNT(*) as node_count FROM pdcas")
            node_count = cursor.fetchone()['node_count']
            
            # Edge count
            cursor.execute("SELECT COUNT(*) as edge_count FROM pdca_relationships")
            edge_count = cursor.fetchone()['edge_count']
            
            # Relationship types
            cursor.execute("""
                SELECT relationship_type, COUNT(*) as count 
                FROM pdca_relationships 
                GROUP BY relationship_type
            """)
            relationship_types = {row['relationship_type']: row['count'] 
                                for row in cursor.fetchall()}
            
            # Most connected nodes
            cursor.execute("""
                SELECT pdca_id, connection_count
                FROM (
                    SELECT from_pdca_id as pdca_id, COUNT(*) as connection_count
                    FROM pdca_relationships
                    GROUP BY from_pdca_id
                    UNION ALL
                    SELECT to_pdca_id as pdca_id, COUNT(*) as connection_count
                    FROM pdca_relationships
                    GROUP BY to_pdca_id
                )
                GROUP BY pdca_id
                ORDER BY SUM(connection_count) DESC
                LIMIT 10
            """)
            most_connected = [dict(row) for row in cursor.fetchall()]
            
            return {
                'node_count': node_count,
                'edge_count': edge_count,
                'relationship_types': relationship_types,
                'most_connected_nodes': most_connected,
                'density': edge_count / (node_count * (node_count - 1)) if node_count > 1 else 0
            }
            
        except Exception as e:
            logger.error(f"Error getting graph stats: {e}")
            return {}
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")


def test_sqlite_graph():
    """Test SQLite graph functionality with sample data."""
    print("Testing SQLite Graph Implementation")
    print("=" * 50)
    
    # Initialize graph
    graph = SQLiteGraph("test_pdca_graph.db")
    
    # Sample PDCA data
    sample_pdcas = [
        {
            'id': '20241027-090000-SaveRestartAgent.ProcessOrchestration',
            'agent_name': 'SaveRestartAgent',
            'agent_role': 'ProcessOrchestration',
            'date': '2024-10-27',
            'timestamp': 1730023200,
            'objective': 'Test objective 1'
        },
        {
            'id': '20241027-100000-BuilderAgent.ComponentDevelopment',
            'agent_name': 'BuilderAgent',
            'agent_role': 'ComponentDevelopment',
            'date': '2024-10-27',
            'timestamp': 1730026800,
            'objective': 'Test objective 2'
        },
        {
            'id': '20241027-110000-TesterAgent.QualityAssurance',
            'agent_name': 'TesterAgent',
            'agent_role': 'QualityAssurance',
            'date': '2024-10-27',
            'timestamp': 1730030400,
            'objective': 'Test objective 3'
        }
    ]
    
    # Add nodes
    print("Adding PDCA nodes...")
    for pdca in sample_pdcas:
        success = graph.add_pdca_node(pdca)
        print(f"  {pdca['id']}: {'✓' if success else '✗'}")
    
    # Add relationships
    print("\nAdding relationships...")
    relationships = [
        ('20241027-090000-SaveRestartAgent.ProcessOrchestration', 
         '20241027-100000-BuilderAgent.ComponentDevelopment'),
        ('20241027-100000-BuilderAgent.ComponentDevelopment', 
         '20241027-110000-TesterAgent.QualityAssurance')
    ]
    
    for from_id, to_id in relationships:
        success = graph.add_relationship(from_id, to_id)
        print(f"  {from_id} -> {to_id}: {'✓' if success else '✗'}")
    
    # Test queries
    print("\nTesting graph queries...")
    
    # Get successors
    successors = graph.get_successors('20241027-090000-SaveRestartAgent.ProcessOrchestration')
    print(f"Successors of SaveRestartAgent: {len(successors)}")
    for s in successors:
        print(f"  -> {s['id']} ({s['agent_name']})")
    
    # Get predecessors
    predecessors = graph.get_predecessors('20241027-110000-TesterAgent.QualityAssurance')
    print(f"Predecessors of TesterAgent: {len(predecessors)}")
    for p in predecessors:
        print(f"  <- {p['id']} ({p['agent_name']})")
    
    # Get breadcrumb navigation
    breadcrumb = graph.get_breadcrumb_navigation('20241027-100000-BuilderAgent.ComponentDevelopment')
    print(f"\nBreadcrumb for BuilderAgent:")
    print(f"  Predecessors: {breadcrumb['predecessor_count']}")
    print(f"  Successors: {breadcrumb['successor_count']}")
    
    # Get graph stats
    stats = graph.get_graph_stats()
    print(f"\nGraph Statistics:")
    print(f"  Nodes: {stats['node_count']}")
    print(f"  Edges: {stats['edge_count']}")
    print(f"  Density: {stats['density']:.3f}")
    
    # Close connection
    graph.close()
    print("\n✓ SQLite Graph test completed successfully!")


if __name__ == "__main__":
    test_sqlite_graph()
