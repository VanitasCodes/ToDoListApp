"""
Utility functions for ToDoListApp.
Helper functions for filtering and sorting tasks.
"""

from datetime import datetime, timedelta


def filter_tasks(tasks, completed=None, priority=None):
    """
    Filter tasks based on completed status and/or priority.
    
    Args:
        tasks: List of Task objects
        completed: True/False/None (None = don't filter)
        priority: 1/2/3/None (None = don't filter)
    
    Returns:
        list: Filtered tasks
    """
    return list(
        filter(
            lambda task: (completed is None or task.completed == completed)
            and (priority is None or task.priority == priority),
            tasks,
        )
    )


def sort_tasks(tasks, key="priority", reverse=False):
    """
    Sort tasks by a given attribute.
    
    Args:
        tasks: List of Task objects
        key: Attribute to sort by ("priority", "title", "deadline")
        reverse: True for descending order
    
    Returns:
        list: Sorted tasks
    """
    return sorted(tasks, key=lambda task: getattr(task, key) or "", reverse=reverse)


def format_tasks(tasks):
    """Format tasks as readable strings."""
    return [
        f"Task {task.id}: {task.title} (Priority: {task.priority}) - {'Done' if task.completed else 'Pending'}"
        for task in tasks
    ]


def get_overdue_tasks(tasks):
    """Get tasks that are past their deadline and not completed."""
    today = datetime.now().strftime("%Y-%m-%d")
    return [
        task for task in tasks
        if task.deadline and task.deadline < today and not task.completed
    ]


def get_tasks_due_soon(tasks, days=7):
    """Get incomplete tasks due within the next X days."""
    today = datetime.now()
    cutoff = (today + timedelta(days=days)).strftime("%Y-%m-%d")
    today_str = today.strftime("%Y-%m-%d")
    
    return [
        task for task in tasks
        if task.deadline and today_str <= task.deadline <= cutoff and not task.completed
    ]


def get_task_stats(tasks):
    """
    Get statistics about tasks.
    
    Returns:
        dict: Stats including total, completed, pending, overdue counts
    """
    total = len(tasks)
    if total == 0:
        return {"total": 0, "completed": 0, "pending": 0, "overdue": 0, "completion_rate": 0.0}
    
    completed = len([t for t in tasks if t.completed])
    overdue = len(get_overdue_tasks(tasks))
    
    return {
        "total": total,
        "completed": completed,
        "pending": total - completed,
        "overdue": overdue,
        "completion_rate": round((completed / total) * 100, 1)
    }