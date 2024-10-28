import toml
import os
import argparse

# Set up CLI argument parser
parser = argparse.ArgumentParser(
    description="Generate Streamlit Howest config with optional CLI arguments.")

parser.add_argument(
    "--base", choices=["light", "dark"], help="Base color mode: light or dark mode")
parser.add_argument(
    "--theme", choices=["blue", "green"], help="Howest theme: Howest blue or Energy Lab green")
parser.add_argument(
    "--stage", choices=["dev", "prod"], help="Project stage: development or production")

args = parser.parse_args()


# ===================================================================


# Helper function to prompt the user for a choice
def get_choice(question: str, choices: list[str], mapping: list):
    """
    Prompts the question and lists the possible answers.\\
    The first answer will always be selected as the default answer.\\
    Returns the relative mapped content.
    """
    if len(choices) != len(mapping):
        raise ValueError("Choices and mapping must have the same length.")
    print("\n" + question)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}", "(default)" if i == 0 else "")
    try:
        choice = input("Number: ").strip()
        choice = 1 if choice == "" else int(choice[0])
    except:
        pass

    while choice not in range(1, len(choices) + 1):
        print("\nInvalid choice. Please try again.")
        try:
            choice = input("Number: ").strip()
            choice = 1 if choice == "" else int(choice[0])
        except:
            pass

    choice_idx = choice - 1
    result = mapping[choice_idx]
    return result


# ===================================================================


# Use CLI args if provided, otherwise prompt user
BASE = args.base if args.base else \
    get_choice(question="Pick your base color mode.",
               choices=["Light mode", "Dark mode"],
               mapping=["light", "dark"])

THEME = args.theme if args.theme else \
    get_choice(question="Pick your Howest theme.",
               choices=["Howest blue", "Energy lab green"],
               mapping=["blue", "green"])

STAGE = args.stage if args.stage else \
    get_choice(question="How would you describe your project stage?",
               choices=["Development", "Production"],
               mapping=["dev", "prod"])


# ===================================================================


# Determine colors based on user input
PRIMARY_COLOR = "#44c8f5" if THEME == "blue" else "#00b140"

if BASE == "light":
    if THEME == "blue":
        PRIMARY_COLOR = "#44c8f5"               # Howest blue
        BACKGROUND_COLOR = "#fafeff"            # very light blue
        SECONDARY_BACKGROUND_COLOR = "#e4f3f7"  # light blue
    elif THEME == "green":
        PRIMARY_COLOR = "#74bf35"               # Energy lab green
        BACKGROUND_COLOR = "#fcfffa"            # very light green
        SECONDARY_BACKGROUND_COLOR = "#e5f2da"  # light green
elif BASE == "dark":
    if THEME == "blue":
        PRIMARY_COLOR = "#3cb1d9"               # slightly darker Howest blue
        BACKGROUND_COLOR = "#1e2030"            # very dark
        SECONDARY_BACKGROUND_COLOR = "#2c3047"  # dark
    elif THEME == "green":
        PRIMARY_COLOR = "#74bf35"               # slightly darker Energy lab green
        BACKGROUND_COLOR = "#1e2030"            # very dark
        SECONDARY_BACKGROUND_COLOR = "#2c3047"  # dark

# Determine Streamlit config
SHOW_ERROR_DETAILS = True if STAGE == "dev" else False
TOOLBAR_MODE = "auto" if STAGE == "dev" else "viewer"

# Build TOML config dictionary
CONFIG = {
    "theme": {
        "base": BASE,
        "primaryColor": PRIMARY_COLOR,
        "backgroundColor": BACKGROUND_COLOR,
        "secondaryBackgroundColor": SECONDARY_BACKGROUND_COLOR
    },
    "browser": {
        "gatherUsageStats": False
    },
    "client": {
        "showErrorDetails": SHOW_ERROR_DETAILS,
        "toolbarMode": TOOLBAR_MODE
    }
}


# ===================================================================


# Write TOML config to file
with open(".streamlit/config.toml", "w") as f:
    toml.dump(CONFIG, f)

print("\n✅ Configuration file '.streamlit/config.toml' created successfully.\n")
