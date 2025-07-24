# 📸 Simple Python Screenshot App

This is a lightweight and user-friendly desktop application built with Python and Tkinter. This tool allows users to quickly capture and save screenshots of their screen with a single click, providing instant visual documentation. It's a great example for beginners to understand basic GUI development and file handling in Python.

---

## ✨ Features

* **Instant Capture:** Take screenshots with a single click.
* **Automatic Naming:** Screenshots are automatically named with a unique timestamp to avoid overwriting.
* **Automatic Directory Creation:** The application automatically creates the designated screenshot directory if it doesn't exist.
* **Simple GUI:** A clean and intuitive graphical user interface (GUI) built with Tkinter.
* **Error Handling:** Basic error handling for screenshot capture failures.
* **Cross-Platform (PyAutoGUI dependent):** While the app itself is Python/Tkinter, `pyautogui`'s screenshot functionality might have platform-specific dependencies (e.g., `Pillow`, `scrot` on Linux).

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
    cd screenshot
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
    This project requires `pyautogui` (which includes `pyscreeze` and `Pillow`).
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Once the dependencies are installed, you can run the application:

```bash
python screenshotapp.py 
