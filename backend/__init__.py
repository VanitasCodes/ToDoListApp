"""
Backend module for ToDoListApp.
Provides database operations and utilities.
"""

from .database import (
    Task,
    add_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    mark_task_complete,
    mark_task_incomplete,
    clear_all_tasks,
    search_tasks,
)

from .utils import (
    filter_tasks,
    sort_tasks,
    format_tasks,
    get_overdue_tasks,
    get_tasks_due_soon,
    get_task_stats,
)

__all__ = [
    "Task",
    "add_task",
    "get_all_tasks",
    "get_task_by_id",
    "update_task",
    "delete_task",
    "mark_task_complete",
    "mark_task_incomplete",
    "clear_all_tasks",
    "search_tasks",
    "filter_tasks",
    "sort_tasks",
    "format_tasks",
    "get_overdue_tasks",
    "get_tasks_due_soon",
    "get_task_stats",
]