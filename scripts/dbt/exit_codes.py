from enum import Enum


class ExitCodes(Enum):
    """Exit Code Enum

    Add to this list in scripts/dbt/exit_codes.py when you want
    to Exit() with a new errorlevel/exitcode"""

    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_GIT_REPOSITORY = 2
