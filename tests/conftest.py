"""Pytest configuration and fixtures."""

import sys
from pathlib import Path

# Add project-root `backend` to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
