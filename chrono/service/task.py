import os
import datetime
def create_job(id, date_str):
    current_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    os.system(f"echo '{current_dir}/python_invoke.sh {id}' | at -m {date_str}")


def validate_datetime(date_str):
    try:
        format_str = '%H:%M %m/%d/%Y'
        datetime.datetime.strptime(date_str, format_str)
    except ValueError:
        return False
    return True

val = input("Enter your value like 14:33 08/20/2020: ")
if validate_datetime(val):
    create_job(1, val)