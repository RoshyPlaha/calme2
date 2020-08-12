import os

def create_job(id):
    os.system(f'echo "/Users/roshy/Documents/projects/calme2/chrono/python_invoke.sh {id}" | at -m 21:25 08/12/2020')

create_job('39393939')