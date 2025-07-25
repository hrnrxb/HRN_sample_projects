import string
import random
import pyperclip # Imports 'pyperclip' for clipboard operations.
import tkinter as tk
from tkinter import messagebox # Imports messagebox for alerts.

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_punctuation=True):
    """Generates a random password with specified configuration."""
    
    # Define character sets based on inclusion flags.
    char_sets = []
    required_chars = []

    if include_uppercase:
        char_sets.append(string.ascii_uppercase)
        required_chars.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        char_sets.append(string.ascii_lowercase)
        required_chars.append(random.choice(string.ascii_lowercase))
    if include_digits:
        char_sets.append(string.digits)
        required_chars.append(random.choice(string.digits))
    if include_punctuation:
        char_sets.append(string.punctuation)
        required_chars.append(random.choice(string.punctuation))

    # Handle cases where no character types are selected.
    if not char_sets:
        messagebox.showwarning("Warning", "At least one character type must be selected.")
        return None
    # Handle case where desired length is too short for required types.
    if length < len(required_chars):
        messagebox.showwarning("Note", "Password length is too short for selected character types.")
        return None

    # Combine all selected characters into a single pool.
    all_chars = []
    for char_set in char_sets:
        all_chars.extend(list(char_set))

    # Build the password list.
    password_list = required_chars[:] # Start with one character from each selected type.
    
    # Fill the remaining length with random characters from the combined pool.
    for _ in range(length - len(required_chars)):
        password_list.append(random.choice(all_chars))

    # Shuffle the entire password list to randomize character positions.
    random.shuffle(password_list)
    
    return "".join(password_list)

class PasswordGeneratorApp:
    """Main application class for the GUI."""
    def __init__(self, master):
        self.master = master
        master.title("Password Generator") # Sets the window title.
        master.geometry("400x450") # Sets the initial window size.
        master.resizable(False, False) # Prevents window resizing.
        master.config(bg="#2C3E50") # Sets a dark background color for the main window.

        # Setup the main frame with internal padding.
        main_frame = tk.Frame(master, bg="#2C3E50", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        # Creates and packs the title label.
        title_label = tk.Label(main_frame, text="Password Generator", font=("Arial", 18, "bold"), fg="#ECF0F1", bg="#2C3E50")
        title_label.pack(pady=10)

        # Frame for password length input.
        length_frame = tk.Frame(main_frame, bg="#2C3E50")
        length_frame.pack(pady=5)
        tk.Label(length_frame, text="Length:", font=("Arial", 12), fg="#ECF0F1", bg="#2C3E50").pack(side=tk.LEFT)
        self.length_entry = tk.Entry(length_frame, width=10, font=("Arial", 12), bg="#34495E", fg="#ECF0F1", insertbackground="#ECF0F1", bd=0, relief="flat")
        self.length_entry.pack(side=tk.LEFT, padx=5)
        self.length_entry.insert(0, "12") # Sets a default password length.

        # Character type checkboxes.
        # BooleanVar is used to track the state (checked/unchecked) of each checkbox.
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.punctuation_var = tk.BooleanVar(value=True)

        # Frame to group character type checkboxes.
        checkbox_frame = tk.LabelFrame(main_frame, text="Include Characters:", font=("Arial", 12, "bold"), fg="#ECF0F1", bg="#2C3E50", bd=2, relief="groove", padx=10, pady=10)
        checkbox_frame.pack(pady=10, fill="x")

        # Create and pack individual checkboxes.
        tk.Checkbutton(checkbox_frame, text="Uppercase (A-Z)", variable=self.uppercase_var, font=("Arial", 11), fg="#ECF0F1", bg="#2C3E50", selectcolor="#2C3E50", activebackground="#34495E", activeforeground="#ECF0F1").pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Lowercase (a-z)", variable=self.lowercase_var, font=("Arial", 11), fg="#ECF0F1", bg="#2C3E50", selectcolor="#2C3E50", activebackground="#34495E", activeforeground="#ECF0F1").pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Digits (0-9)", variable=self.digits_var, font=("Arial", 11), fg="#ECF0F1", bg="#2C3E50", selectcolor="#2C3E50", activebackground="#34495E", activeforeground="#ECF0F1").pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Punctuation (!@#$)", variable=self.punctuation_var, font=("Arial", 11), fg="#ECF0F1", bg="#2C3E50", selectcolor="#2C3E50", activebackground="#34495E", activeforeground="#ECF0F1").pack(anchor="w")

        # Creates the "Generate Password" button.
        generate_button = tk.Button(main_frame, text="Generate Password", command=self.generate_and_display_password, font=("Arial", 14, "bold"), bg="#27AE60", fg="white", bd=0, relief="raised", padx=15, pady=8)
        generate_button.pack(pady=15)

        # Entry widget to display the generated password.
        self.password_display = tk.Entry(main_frame, width=35, font=("Arial", 14), fg="#2C3E50", bg="#ECF0F1", bd=0, relief="flat", justify="center")
        self.password_display.pack(pady=10)

        # Creates the "Copy to Clipboard" button.
        copy_button = tk.Button(main_frame, text="Copy to Clipboard", command=self.copy_password, font=("Arial", 12), bg="#3498DB", fg="white", bd=0, relief="raised", padx=10, pady=5)
        copy_button.pack(pady=5)

    def generate_and_display_password(self):
        """Gets user input and displays the generated password."""
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showwarning("Tip", "Password length must be positive!")
                return

            password = generate_password(
                length,
                self.uppercase_var.get(),
                self.lowercase_var.get(),
                self.digits_var.get(),
                self.punctuation_var.get()
            )
            
            if password:
                self.password_display.delete(0, tk.END) # Clears any previous password.
                self.password_display.insert(0, password) # Displays the newly generated password.
            else:
                self.password_display.delete(0, tk.END)
                self.password_display.insert(0, "Error generating password.") # Shows error message if generation fails.

        except ValueError:
            messagebox.showerror("Warning", "Invalid length! Please enter a number.")

    def copy_password(self):
        """Copies the displayed password to the clipboard."""
        password = self.password_display.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Note", "Password copied to clipboard!")
            except pyperclip.PyperclipException:
                messagebox.showerror("Problem", "Could not copy to clipboard. Pyperclip might need xclip/xsel on Linux.")
        else:
            messagebox.showwarning("Tip", "No password to copy!")

# Runs the main application when the script is executed.
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
