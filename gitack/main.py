from gitack import loader
from gitack import ui
from gitack import constants
from gitack import validation

from dotenv import load_dotenv


def init(project_names, common_cats):
    common_questions = loader.load_questions(
        parent_key=constants.YAML_CONSTANTS.COMMON_KEY, 
        child_keys=common_cats
    )
    project_questions = loader.load_questions(
        parent_key=constants.YAML_CONSTANTS.PROJECT_KEY, 
        child_keys=project_names
    )
    all_questions = common_questions + project_questions
    results = ui.ask_questions(all_questions)
    ui.display_summary(results)

def main():
    print(__name__)
    validation.validate_env()

    common_cats = ui.ask_choice_from_user(
        input_key=constants.YAML_CONSTANTS.COMMON_KEY, 
        message_for_user=constants.USER_MESSAGES.COMMON_CATS
    )
    projects = ui.ask_choice_from_user(
        input_key=constants.YAML_CONSTANTS.PROJECT_KEY, 
        message_for_user=constants.USER_MESSAGES.PROJECTS
    )
    init(project_names=projects, common_cats=common_cats)

if __name__ == "__main__":
    # Loads environment variables via .env file
    # The value of a variable is the first of the values defined in the following list:
        # Value of that variable in the environment.
        # Value of that variable in the .env file.
    load_dotenv()
    main()
