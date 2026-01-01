#!/usr/bin/env python3
"""
ToDoListApp - Main Entry Point

A simple yet powerful task management application.
Run this file to start the app: python main.py
"""

import sys
import logging

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Initialize and run the ToDoListApp."""
    logger.info("Starting ToDoListApp...")
    
    # Enable High DPI scaling for Windows 11
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    # Create the application
    app = QApplication(sys.argv)
    app.setApplicationName("ToDoListApp")
    app.setApplicationVersion("1.0.0")
    
    # Import here to avoid circular imports
    from frontend.gui import ToDoApp
    
    # Create and show the main window
    window = ToDoApp()
    window.show()
    
    logger.info("Application window opened")
    
    # Run the app
    sys.exit(app.exec())


if __name__ == "__main__":
    main()