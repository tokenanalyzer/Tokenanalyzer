import json
import os
import time
from datetime import datetime

VIP_FILE = os.path.expanduser("~/vip_data.json")
LOG_FILE = os.path.expanduser("~/remove_expired_vips.log")

def log_message(message):
    """Log messages to a file with timestamps."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def remove_expired_vips():
    """Remove expired VIP users from the JSON file."""
    log_message("VIP removal script started!")

    if not os.path.exists(VIP_FILE):
        log_message("VIP file not found!")
        return

    try:
        with open(VIP_FILE, "r") as file:
            data = json.load(file)

        if "users" not in data or not isinstance(data["users"], list):
            log_message("Invalid JSON format! 'users' list missing.")
            return

        current_time = datetime.now().timestamp()
        updated_users = [
            user for user in data["users"]
            if datetime.strptime(user["expiry"], "%Y-%m-%d").timestamp() > current_time
        ]

        data["users"] = updated_users  # Update the list

        with open(VIP_FILE, "w") as file:
            json.dump(data, file, indent=4)

        log_message(f"Expired VIPs removed! Remaining users: {len(updated_users)}")
    
    except Exception as e:
        log_message(f"Error: {str(e)}")

    log_message("VIP removal script completed!")

if __name__ == "__main__":
    remove_expired_vips()
