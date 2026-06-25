import subprocess
import time
from datetime import datetime

def run_app():
    """Function to run the app and monitor its process."""
    while True:
        # Start the process
        print("Starting the app...")
        process = subprocess.Popen(["python3", "-m", "pipenv", "run", "./app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Monitor the process
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            # If the process ends with an error, record the reason and time to the log file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"App stopped at {timestamp} with an error:\n{stderr.decode()}\n"
            print(error_message)
            with open("app_error.log", "a") as log_file:
                log_file.write(error_message)
        else:
            # If the process ends successfully, record the time to the log file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            success_message = f"App stopped at {timestamp} without errors.\n"
            print(success_message)
            with open("app_log.log", "a") as log_file:
                log_file.write(success_message)

        # Wait for a while before restarting the app
        print("Waiting to restart the app...")
        time.sleep(5)  # Adjust this time according to your needs

if __name__ == "__main__":
    run_app()
