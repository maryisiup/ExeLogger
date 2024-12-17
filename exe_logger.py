import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import os
import datetime

class ExecutableLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ExeLogger - Executable File Logger")
        self.root.geometry("600x400")
        
        # File for saving logs
        self.log_file = "exe_logger_log.txt"

        # Main Label
        main_label = tk.Label(self.root, text="Running Executables", font=("Helvetica", 14))
        main_label.pack(pady=10)
        
        # Treeview for process details
        columns = ("PID", "Process Name", "Path")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("PID", text="PID")
        self.tree.heading("Process Name", text="Process Name")
        self.tree.heading("Path", text="Execution Path")
        self.tree.column("PID", width=50, anchor="center")
        self.tree.column("Process Name", width=150, anchor="center")
        self.tree.column("Path", width=350, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Refresh Button
        refresh_button = tk.Button(self.root, text="Refresh", command=self.refresh_executables)
        refresh_button.pack(pady=5)
        
        # Exit Button
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.pack(pady=5)

        # Initial Load
        self.refresh_executables()

    def get_running_executables(self):
        """Retrieves running executables and returns a list."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if proc.info['exe']:  # Only include processes with a valid execution path
                    processes.append((proc.info['pid'], proc.info['name'], proc.info['exe']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return processes

    def log_executables(self, processes):
        """Logs the running executables to a file."""
        with open(self.log_file, "a") as log:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"\n[Log Time: {timestamp}]\n")
            for pid, name, path in processes:
                log.write(f"PID: {pid}, Name: {name}, Path: {path}\n")
            log.write("\n")

    def refresh_executables(self):
        """Refreshes the TreeView with the current list of running executables."""
        self.tree.delete(*self.tree.get_children())  # Clear previous entries
        processes = self.get_running_executables()
        
        # Insert data into TreeView
        for pid, name, path in processes:
            self.tree.insert("", "end", values=(pid, name, path))
        
        # Log data
        self.log_executables(processes)
        messagebox.showinfo("Refreshed", "The list of executables has been updated and logged.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExecutableLoggerApp(root)
    root.mainloop()






































































