# 🔒 Python Password Generator GUI

This is a simple, yet robust, desktop application built with Python and Tkinter. It allows users to generate strong, random passwords based on customizable criteria such as length and character types (uppercase, lowercase, digits, punctuation). The generated password can be easily copied to the clipboard. This project is ideal for understanding basic GUI development, user input validation, and secure password generation principles in Python.

---

## ✨ Features

* **Customizable Length:** Generate passwords of any desired length.
* **Selectable Character Types:** Choose to include uppercase letters, lowercase letters, digits, and/or punctuation marks.
* **Guaranteed Character Inclusion:** Ensures that at least one character from each selected type is present in the generated password (if length permits).
* **User-Friendly GUI:** A clean and intuitive graphical interface built with Tkinter.
* **Copy to Clipboard:** Easily copy the generated password to your system clipboard with a single click.
* **Input Validation:** Robust handling of user input for password length.
* **Error & Warning Messages:** Provides clear feedback to the user through pop-up messages.

---

## 🚀 Getting Started

Follow these steps to get the application up and running on your local machine.

### Prerequisites

Before you begin, ensure you have Python installed. This project is tested with Python 3.11+.

* **Python 3.11+** (Recommended: [Download Python](https://www.python.org/downloads/))

### Installation

1.  **Clone the repository:**
    First, clone your main repository (e.g., `HRN_Sample_Projects`) to your local machine.
    ```bash
    git clone https://github.com/hrnrxb/HRN_sample_projects
    cd HRN_Sample_Projects
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd password_generator
    ```
3.  **Create a Python Virtual Environment (Recommended):**
    It's highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.
    ```bash
    python3 -m venv env
    # Activate the virtual environment:
    # On macOS / Linux:
    source env/bin/activate
    # On Windows:
    # .\env\Scripts\activate
    ```
4.  **Install dependencies:**
    This project requires `pyperclip`.
    ```bash
    pip install -r requirements.txt
    ```
    

### Running the Application

Once the dependencies are installed, you can run the application:

```bash
python password_generator_app.py # Or whatever your main script is named, e.g., main.pyb
```
A Tkinter window titled "Password Generator" will appear, allowing you to generate and manage passwords.
