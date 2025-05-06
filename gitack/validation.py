from gitack import constants
import os
import pathlib

def validate_env():
    """
    Check if mandatory environment variables are present in environment or not.
    If not present, raise an exception

    TODO : I want to make it in a way where I can validate all variables and tell user to fix all at once
    """
    for var in constants.ENV_VARIABLES.MANDATORY_VARS:
        value = os.environ.get(var,None)
        if value == None:
            raise Exception(f"Missing mandatory environment variable : {var}")
        is_valid, err_msg = constants.ENV_VARIABLES.ENV_VALIDATE_MAP[var]()
        if not is_valid:
            raise Exception(err_msg)

def validate_gitackconfig_variable():
    filepath = pathlib.Path(os.environ[constants.ENV_VARIABLES.GITACKCONFIG])
    if pathlib.Path.is_file(filepath):
        return True, None
    return False, f"File '{filepath}' does not exist"