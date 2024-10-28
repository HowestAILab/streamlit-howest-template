#!/bin/bash

# Configure Poetry environment
clear
bash .devcontainer/scripts/create_python_env.sh

# Feel free to add setup commands here, they will run once after (re)building the devcontainer
poetry run python change_config_script.py --base=light --theme=blue --stage=dev
poetry run streamlit run example.py

poetry shell