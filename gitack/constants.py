from questionary import Style
from gitack import validation

class QuestionaryStyles:
    BIG_LINE = "-----------------------------------------------"
    DESCRIPTION_SYMBOL = "*"
    REFERENCE_SYMBOL = ">"
    DONE_SYMBOL = "✅"
    NOT_DONE_SYMBOL = "❌"
    STYLE_CHOICES_QUESTION = Style([
        ('highlighted', 'fg:#f44336 bold underline')
    ])

class QuestionTypes:
    YESNO = "yesno"
    TEXT = "text"
    VALID_QUESTION_TYPES = {YESNO,TEXT}

class YAML_CONSTANTS:
    FILEPATH = "YAML_FILES/questions.yaml"
    COMMON_KEY = "common"
    PROJECT_KEY = "projects"
    QUESTIONS_KEY = "questions"

class USER_MESSAGES:
    COMMON_CATS = "Select categories"
    PROJECTS = "Select projects"

class ENV_VARIABLES:
    GITACKCONFIG="GITACKCONFIG"
    MANDATORY_VARS = [GITACKCONFIG]
    # TODO : Make a better design
    # This map is used to map "env variable" -> validation function 
    ENV_VALIDATE_MAP = {
        GITACKCONFIG : validation.validate_gitackconfig_variable
    }