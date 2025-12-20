import pytest
from pathlib import Path
from app import config

@pytest.fixture
def temp_projects_dir(tmp_path: Path):
    original = config.PROJECTS_DIR
    config.PROJECTS_DIR = tmp_path
    yield tmp_path
    config.PROJECTS_DIR = original
