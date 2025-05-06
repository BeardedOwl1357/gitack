import yaml
from gitack import constants
import os

def _get_yaml_object(parent_key,):
    filepath = os.environ[constants.ENV_VARIABLES.GITACKCONFIG]
    with open(filepath,"r") as f: 
        y = yaml.safe_load(f)
        return y.get(parent_key,{})

def load_questions(parent_key, child_keys):
    output = []
    parent_questions = _get_yaml_object(parent_key)
    for child_key in child_keys:
        # If 'questions' key exists in YAML but does not have any value, it's read as None. We use `or []` to deal with this
        # If key does not exist, default value is []
        questions = parent_questions.get(child_key,{}).get(constants.YAML_CONSTANTS.QUESTIONS_KEY,[]) or []
        output.extend(questions)
    return output
            

def list_keys_of_yaml_file(input_key):
    yaml_object = _get_yaml_object(input_key)
    ans = yaml_object.keys()
    return ans