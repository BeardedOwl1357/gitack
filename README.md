# Gitack : Git Acknowledge

- This is a cli tool I am working on to ensure that I don't forget to include the common checks before I push my code to the working branch. Pretty much born because of my tendencies to forget things
- It uses a YAML file to define rules. There are two types of rules
  - common : Common can be subdivided into categories. This is used to indicate checks that are common to a "branch" of developers. For example, there are some checks that are common to backend developers, some are common to frontend developers etc. These are defined by `common` key in the YAML file 
  - project : They are project specific checks. It is possible that you are working on multiple projects and each project has its quirks / things to be checked. 


> [!tip]
> Demonstration of tool : <a href="https://www.youtube.com/watch?v=VlwZCaTqPZU" target="_blank"> https://www.youtube.com/watch?v=VlwZCaTqPZU </a>

A sample of YAML file can be accessed from here : [questions.yaml](./gitack/YAML_FILES/questions.yaml). More info about YAML file is defined in [yaml](#yaml-file) section

## Installation (TODO. Need to publish on pypi)

## yaml file
A "question" is defined as follows
```yaml
type: yesno
name : "Dashboard API regression"
question: "If dashboard changes have been done, is there any API that has been affected?"
description: |
  - To test this
    - Create sample data for each portlet (edge might be an exception. Or just use a DB link)
    - Open UI and check for both ECPAdmin and GBUAdmin
reference: ""
expected: "N"
errorMsg : "Check for regression in lower environments. It's difficult to fix on higher environments"
```

- `type` : Type of question. The supported types are `yesno` and `text`. A `yesno` question has a binary answer (`Y` or `N`) and a `text` question accepts a string as an answer
- `name` : Name of the question.  This is used primarily in the summary table that is generated at the end
- `question` : The prompt that is asked to the user
- `description` : Description or background for a question. Can be written in markdown as it will be rendered in markdown
- `reference` : Optional placeholder. Can be used to provide a reference of a URL or book or anything that provides more context
- `expected` : For a `yesno` question, what is the expected answer?
- `errorMsg` : In case a user's answer does not match with `expected` answer, this `errorMsg` will be displayed. It is optional 

## Local development setup

This project uses a Python virtual environment to manage dependencies. Follow the steps below to set up the environment and install the required packages.

### 🐍 Create a Virtual Environment

```bash
# Give execution permissions
chmod +x ./install_deps.sh ;

# Run it
./install_deps.sh;
```

### Activate venv and run script

```bash
source venv/bin/activate ;
# To check if venv is activate or not, this command should have an output
echo $VIRTUAL_ENV;
```

### Run the program
```bash
# Assuming that you are on root of repo
# This variable is mandatory
export GITACKCONFIG="YAML_FILES/questions.yaml";
python3 -m gitack.main ;
```