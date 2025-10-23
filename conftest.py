"""
pytest configuration file for adding the project root to sys.path

This allows pytest to discover and import the evaluators module
"""

import sys
from pathlib import Path

# Add the project root to sys.path so pytest can find 'evaluators'
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
