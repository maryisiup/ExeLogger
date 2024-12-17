# ExeLogger - Executable File Logger

**ExeLogger** is a Windows-based tool that monitors and logs all running executable processes in real-time. It features a graphical user interface (GUI) and allows users to refresh the list and log the processes to a file.

---

## Features:
1. **GUI Interface**: View all currently running executable processes.
2. **Real-time Logging**: Logs process details (PID, name, and execution path) to a log file.
3. **Refresh Option**: Update the list of executables on demand.
4. **Log File**: Saves logs to a file named `exe_logger_log.txt`.

---

## Requirements:
- **Python 3.x**
- **Dependencies**:
   - `psutil` (for process monitoring)
   - `tkinter` (for GUI)

---

## How It Works:
1. Launch the program.
2. The tool displays all running executables, including:
   - **Process ID (PID)**
   - **Process Name**
   - **Execution Path**
3. Click **Refresh** to update the list and log the current state to the file.
4. Logs are automatically saved with timestamps in the file `exe_logger_log.txt`.


---

## Notes:
- Requires administrative privileges for processes running with elevated permissions.
- Designed for Windows systems.
