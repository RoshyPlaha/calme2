import os
import datetime
def create_job(id, date_str):
    try: 
        current_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        os.system(f"echo '{current_dir}/python_invoke.sh {id}' | at -m {date_str}")
        print(f'created new task id {id} for future: {date_str}')
    except Error:
        print(f'Unable to make job for id {id}')
        return False
    return True

def validate_datetime(date_str):
    try:
        format_str = '%H:%M %m/%d/%Y'
        datetime.datetime.strptime(date_str, format_str)
    except ValueError:
        return False
    return True

# val = input("Enter your value like 14:33 08/20/2020: ")
# if validate_datetime(val):
#     create_job('3', val)