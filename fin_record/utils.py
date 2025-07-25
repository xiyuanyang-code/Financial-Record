from datetime import datetime

def get_date():
    # get today's date
    return datetime.now().strftime("%Y-%m-%d")