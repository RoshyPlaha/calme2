import os
import datetime
def create_job(id, datetime):
    os.system(f"echo '/Users/roshy/Documents/projects/calme2/chrono/python_invoke.sh {id}' | at -m {datetime}")

# create_job('39393939')

def validate_datetime(date_str):
    try:
        format_str = '%H:%M %m/%d/%Y'
        datetime.datetime.strptime(date_str, format_str)
    except ValueError:
        return False
    return True


val = input("Enter your value like 15:46 08/18/2020: ")
if validate_datetime(val):
    create_job(1, val)