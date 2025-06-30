from datetime import datetime

def get_formatted_timestamp():
    """
    Returns current timestamp in YYYY-MM-DD HH:MM:SS format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
