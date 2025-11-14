import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool
import os
from datetime import datetime
from typing import Optional, Dict, List
import threading

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres.pkcgaqepkhudtgxadmsw:Caroline2019%40@aws-0-us-west-2.pooler.supabase.com:6543/postgres")

if "[YOUR-PASSWORD]" in DATABASE_URL or "[Caroline2019@]" in DATABASE_URL:
    print("⚠️  AVISO: Configure a variável de ambiente DATABASE_URL com sua senha!")
    print("   Exemplo: export DATABASE_URL='postgresql://postgres.pkcgaqepkhudtgxadmsw:SUA_SENHA@aws-0-us-west-2.pooler.supabase.com:6543/postgres'")

pool = None
pool_lock = threading.Lock()

def get_pool():
    global pool
    if pool is None:
        with pool_lock:
            if pool is None:
                pool = ThreadedConnectionPool(1, 20, DATABASE_URL)
    return pool

def init_database():
    conn = None
    try:
        pool = get_pool()
        conn = pool.getconn()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_extractions (
                id SERIAL PRIMARY KEY,
                start_url TEXT NOT NULL,
                tool_name VARCHAR(255) NOT NULL DEFAULT 'MyAPI',
                api_base_url TEXT NOT NULL,
                status VARCHAR(50) NOT NULL DEFAULT 'pending',
                output_path TEXT,
                error_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                processed_at TIMESTAMP,
                endpoint_count INTEGER
            )
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_status ON api_extractions(status);
            CREATE INDEX IF NOT EXISTS idx_created_at ON api_extractions(created_at);
        """)
        
        conn.commit()
        cursor.close()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            pool.putconn(conn)

def create_extraction(data: Dict) -> Optional[int]:
    conn = None
    try:
        pool = get_pool()
        conn = pool.getconn()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO api_extractions (start_url, tool_name, api_base_url, status)
            VALUES (%s, %s, %s, 'pending')
            RETURNING id
        """, (data['startUrl'], data['toolName'], data['apiBaseUrl']))
        
        extraction_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return extraction_id
    except Exception as e:
        print(f"Error creating extraction: {e}")
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            pool.putconn(conn)

def get_pending_extractions(limit: int = 10) -> List[Dict]:
    conn = None
    try:
        pool = get_pool()
        conn = pool.getconn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute("""
            SELECT * FROM api_extractions
            WHERE status = 'pending'
            ORDER BY created_at ASC
            LIMIT %s
        """, (limit,))
        
        results = cursor.fetchall()
        cursor.close()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting pending extractions: {e}")
        return []
    finally:
        if conn:
            pool.putconn(conn)

def update_extraction_status(extraction_id: int, status: str, output_path: Optional[str] = None, 
                            error_message: Optional[str] = None, endpoint_count: Optional[int] = None):
    conn = None
    try:
        pool = get_pool()
        conn = pool.getconn()
        cursor = conn.cursor()
        
        update_fields = ["status = %s", "updated_at = CURRENT_TIMESTAMP"]
        values = [status]
        
        if output_path:
            update_fields.append("output_path = %s")
            values.append(output_path)
        
        if error_message:
            update_fields.append("error_message = %s")
            values.append(error_message)
        
        if endpoint_count is not None:
            update_fields.append("endpoint_count = %s")
            values.append(endpoint_count)
        
        if status == 'completed':
            update_fields.append("processed_at = CURRENT_TIMESTAMP")
        
        values.append(extraction_id)
        
        query = f"UPDATE api_extractions SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(query, values)
        
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error updating extraction status: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            pool.putconn(conn)

def get_extraction(extraction_id: int) -> Optional[Dict]:
    conn = None
    try:
        pool = get_pool()
        conn = pool.getconn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute("SELECT * FROM api_extractions WHERE id = %s", (extraction_id,))
        result = cursor.fetchone()
        cursor.close()
        
        return dict(result) if result else None
    except Exception as e:
        print(f"Error getting extraction: {e}")
        return None
    finally:
        if conn:
            pool.putconn(conn)

def get_all_extractions(limit: int = 50) -> List[Dict]:
    conn = None
    try:
        pool = get_pool()
        conn = pool.getconn()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute("""
            SELECT * FROM api_extractions
            ORDER BY created_at DESC
            LIMIT %s
        """, (limit,))
        
        results = cursor.fetchall()
        cursor.close()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting all extractions: {e}")
        return []
    finally:
        if conn:
            pool.putconn(conn)

