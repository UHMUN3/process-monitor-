import psutil

def display_process_info():
    """
    Retrieves and displays information about all active system processes.
    Including safety checks to prevent crashes when values are equal to None.
    """
    # Define column headers with consistent spacing
    header = f"{'PID':<10} {'Name':<25} {'Memory %':<10} {'CPU %':<10}"
    print(header)
    print("-" * len(header))
    
    # Iterate through all running processes
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
        try:
            #Use .get() and 'if is not None' to handle restricted processes
            pid = proc.info.get('pid') or 0
            name = proc.info.get('name') or "N/A"
            
            # This is the "Safety Block" that prevents the NoneType error
            mem = proc.info.get('memory_percent') if proc.info.get('memory_percent') is not None else 0.0
            cpu = proc.info.get('cpu_percent') if proc.info.get('cpu_percent') is not None else 0.0

            # Having verified that ‘mem’ and ‘cpu’ are numeric values (0.0), the code will no longer encounter a crash.
            print(f"{pid:<10} {name:<25} {mem:<10.2f} {cpu:<10.2f}")
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    # Entry point for the script
    display_process_info()