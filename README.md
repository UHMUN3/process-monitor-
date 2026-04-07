# System Process Monitor

A lightweight Python utility that provides a real-time snapshot of active system processes. This script leverages the `psutil` library to retrieve critical performance metrics while maintaining high stability through robust error handling.

---

## 🚀 Features

* **Real-time Process Listing:** Iterates through all active system processes.
* **Performance Metrics:** Displays memory and CPU consumption as percentages.
* **Crash-Resistant Design:** Handles `NoneType` values for restricted processes.
* **Graceful Error Handling:** Skips processes with access restrictions or those that terminate during execution.

---

## 🛠️ Requirements

Ensure you have the `psutil` library installed:

```bash
pip install psutil

Run the script from your terminal:

python process_monitor.py