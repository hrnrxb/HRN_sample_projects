import time
import pyautogui as ss
import tkinter as tk
import os # Import 'os' for path operations.

def screenshot():
    """Captures and saves a screenshot."""
    timestamp = int(round(time.time() * 1000))
    
    # Define output directory.
    output_directory = "\\screenshot\\screenshot data"
    
    # Create directory if it doesn't exist.
    os.makedirs(output_directory, exist_ok=True)
    
    # Construct full file path.
    file_path = os.path.join(output_directory, f"{timestamp}.png") 

    # time.sleep(0.1)   # Commented because it should take screenshot instantly.
    
    try:
        # Take and show screenshot.
        img = ss.screenshot(file_path)
        img.show() 
        print(f"Screenshot saved to: {file_path}") # User feedback.
    except Exception as e:
        # Handle screenshot errors.
        print(f"Error taking screenshot: {e}")


# Run app when script is executed.
if __name__ == "__main__":
    # Setup main Tkinter window.
    root = tk.Tk()
    root.title("Screenshot App") 

    # Create frame for buttons.
    frame = tk.Frame(root)
    frame.pack(pady=20) 

    # Create 'Take SS' button.
    button = tk.Button(
        frame,
        text = "Take SS",
        command = screenshot, 
        bg = "#4CAF50", 
        fg = "white",   
        font = ("Arial", 12, "bold"), 
        padx = 10,      
        pady = 5        
    )
    button.pack(side = tk.LEFT, padx=10) 

    # Create 'Exit' button.
    close = tk.Button(
        frame,
        text = "Exit",
        command = root.destroy, # Closes the Tkinter window.
        bg = "#F44336", 
        fg = "white",   
        font = ("Arial", 12, "bold"), 
        padx = 10,
        pady = 5
    )
    close.pack(side = tk.LEFT, padx=10) 

    # Start the GUI.
    root.mainloop()