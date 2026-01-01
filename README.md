# ✅ ToDoListApp

A simple yet powerful task management application built with Python, PySide6, and SQLAlchemy.

## ✨ Features

- ✅ Create, edit, and delete tasks
- 📅 Set deadlines with color-coded warnings (red=overdue, orange=soon, green=safe)
- 🔍 Search and filter tasks
- 🌓 Automatic dark/light mode (Windows 11)
- 💾 SQLite database persistence
- 📤 Export/Import tasks as JSON
- 📊 Sort by priority or title

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Windows 11 (for auto theme detection)

### Installation

```powershell
# Clone the repo
git clone https://github.com/yourusername/ToDoListApp.git
cd ToDoListApp

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

## 📁 Project Structure

```
ToDoListApp/
├── backend/
│   ├── __init__.py      # Package exports
│   ├── database.py      # SQLAlchemy database operations
│   └── utils.py         # Helper functions
├── frontend/
│   └── gui.py           # PySide6 GUI
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── tasks.db             # SQLite database
└── tasks.json           # Export file
```

## 🎨 Priority Levels

| Level | Color  | Meaning         |
| ----- | ------ | --------------- |
| 1     | Green  | Low priority    |
| 2     | Yellow | Medium priority |
| 3     | Red    | High priority   |

## 📄 License

MIT License - Use freely!
