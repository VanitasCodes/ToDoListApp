"""
Database module for ToDoListApp.
Handles all database operations using SQLAlchemy ORM.
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from contextlib import contextmanager
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_PATH = os.getenv("TODO_DB_PATH", "tasks.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base class for models
Base = declarative_base()

# Thread-safe session factory
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class Task(Base):
    """Task model - represents a todo item in the database."""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    priority = Column(Integer, default=1)  # 1=Low, 2=Medium, 3=High
    completed = Column(Boolean, default=False)
    deadline = Column(String, nullable=True)  # Format: "YYYY-MM-DD"

    def __repr__(self):
        status = "✓" if self.completed else "○"
        return f"<Task {self.id}: [{status}] {self.title}>"

    def to_dict(self):
        """Convert task to dictionary for JSON export."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "deadline": self.deadline
        }


# Create tables
Base.metadata.create_all(bind=engine)


@contextmanager
def get_db():
    """Context manager for database sessions."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database error: {e}")
        raise
    finally:
        db.close()


# =============================================================================
# CRUD OPERATIONS
# =============================================================================

def add_task(title: str, priority: int = 1, deadline: str = None) -> dict:
    """
    Add a new task to the database.
    
    Args:
        title: Task title (required)
        priority: 1=Low, 2=Medium, 3=High (default: 1)
        deadline: Due date as "YYYY-MM-DD" string (optional)
    
    Returns:
        dict: The created task
    """
    with get_db() as db:
        new_task = Task(title=title, priority=priority, deadline=deadline)
        db.add(new_task)
        db.flush()
        logger.info(f"Created: {new_task}")
        return new_task.to_dict()


def get_all_tasks() -> list:
    """Get all tasks from the database."""
    with get_db() as db:
        tasks = db.query(Task).all()
        # Detach from session
        db.expunge_all()
        return tasks


def get_task_by_id(task_id: int):
    """Get a specific task by ID."""
    with get_db() as db:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            db.expunge(task)
        return task


def update_task(task_id: int, **kwargs) -> bool:
    """
    Update a task's fields.
    
    Args:
        task_id: ID of task to update
        **kwargs: Fields to update (title=, priority=, deadline=, completed=)
    
    Returns:
        bool: True if successful
    """
    with get_db() as db:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            logger.info(f"Updated task {task_id}: {kwargs}")
            return True
        return False


def mark_task_complete(task_id: int) -> bool:
    """Mark a task as completed."""
    return update_task(task_id, completed=True)


def mark_task_incomplete(task_id: int) -> bool:
    """Mark a task as not completed."""
    return update_task(task_id, completed=False)


def delete_task(task_id: int) -> bool:
    """Delete a task by ID."""
    with get_db() as db:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            db.delete(task)
            logger.info(f"Deleted task {task_id}")
            return True
        return False


def clear_all_tasks() -> int:
    """Delete all tasks. Returns count deleted."""
    with get_db() as db:
        count = db.query(Task).delete()
        logger.info(f"Cleared {count} tasks")
        return count


def search_tasks(query: str) -> list:
    """Search tasks by title."""
    with get_db() as db:
        tasks = db.query(Task).filter(Task.title.ilike(f"%{query}%")).all()
        db.expunge_all()
        return tasks