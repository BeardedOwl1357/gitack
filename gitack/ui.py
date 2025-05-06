import questionary
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from gitack import constants
import os
from gitack import loader

console = Console()

def choices_question(message, choices, binary=False) -> str:
    if binary == True:
        return questionary.select(
            message=message,
            choices=choices,
            use_arrow_keys=True,
            style=constants.QuestionaryStyles.STYLE_CHOICES_QUESTION
        ).unsafe_ask()
    return questionary.checkbox(
        message=message,
        choices=choices,
        use_arrow_keys=True,
        style=constants.QuestionaryStyles.STYLE_CHOICES_QUESTION
    ).unsafe_ask()

def clear_screen():
    """Clear the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_choice_from_user(input_key, message_for_user):
    choices = loader.list_keys_of_yaml_file(input_key=input_key)
    clear_screen()
    user_choices = choices_question(
        message=message_for_user, 
        choices=choices
    )
    return user_choices


# TODO : Make question a class
def ask_questions(questions):
    results = []
    for q in questions:
        q_name = q.get("name","")
        q_type = q.get("type")
        question = q.get("question", "Unnamed question")
        description = q.get("description", "")
        md_description = Markdown(description)
        reference = q.get("reference", "")
        expected = q.get("expected", "")
        # Clear screen before asking each question
        clear_screen()

        console.print(Markdown(f"# {q_name}"))
        console.print(md_description)

        console.print("\n\n\n")
        if reference:
            console.print(f"{constants.QuestionaryStyles.REFERENCE_SYMBOL} Reference: {reference}", style="yellow")

        # Ask the question based on its type
        q_type = q_type.lower()
        if q_type not in constants.QuestionTypes.VALID_QUESTION_TYPES:
            raise Exception("Invalid question type")

        answer = None
        if q_type == constants.QuestionTypes.YESNO:
            answer = choices_question(
                message=question, 
                choices=["Y", "N"],
                binary=True
            )
        elif q_type == constants.QuestionTypes.TEXT:
            answer = questionary.text(question).unsafe_ask()

        # Evaluate the answer
        passed = (answer == expected)
        error_msg = q.get("errorMsg","You should handle this")
        if passed == False:
            console.print("\n\n")
            console.print(f"Answer '{answer}' is not expected. {error_msg} ",style="bold red")
            console.print("\n\n")
            questionary.press_any_key_to_continue().unsafe_ask()

        results.append((q_name,question, answer, passed))
    return results

def display_summary(results):
    # Create a table using rich
    clear_screen()
    table = Table(show_header=True, header_style="bold cyan")

    # Add columns with styles
    table.add_column("Name", justify="left", max_width=20)
    table.add_column("Question", justify="left", max_width=30)
    table.add_column("Is valid?", justify="center", style="bold")

    # Add rows with status-based coloring
    for name,q, a, ok in results:
        status = constants.QuestionaryStyles.DONE_SYMBOL if ok else constants.QuestionaryStyles.NOT_DONE_SYMBOL
        # status_style = Style(color="green") if ok else Style(color="red")
        table.add_row(name,q, status)
        table.add_row("","","")

    # Style the table border and padding
    table.border = True
    table.expand = True
    table.padding = (0, 2)

    # Display the table with rich console
    console.print(table)