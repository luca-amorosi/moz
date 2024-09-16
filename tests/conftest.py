import sys
import shutil
from pathlib import Path

import pytest

import maya.standalone

FILE_PATH = Path(__file__)


def pytest_sessionstart(session: pytest.Session):
    import_module()
    maya.standalone.initialize()


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    maya.standalone.uninitialize()
    clean_maya_app_dir()


def import_module():
    module_dir = FILE_PATH.parents[1].joinpath("python").resolve()
    sys.path.append(module_dir.as_posix())


def clean_maya_app_dir():
    """Delete files created during test session in temp/maya directory."""
    maya_temp_dir = FILE_PATH.parents[0].joinpath("temp", "maya")
    shutil.rmtree(maya_temp_dir)

    # Recreate maya folder.
    maya_temp_dir.mkdir()


@pytest.fixture(scope="function")
def maya_scene():
    from maya import cmds

    # Create a new Maya scene
    cmds.file(new=True, force=True)

    yield

    # Clean up the scene after the tests
    cmds.file(new=True, force=True)
