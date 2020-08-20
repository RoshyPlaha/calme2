from app import app
from flask import request
from service import task

@app.route('/')
@app.route('/index')
def index():
    return "Unused"

@app.route('/v1/job', methods=["POST"])
def post_job():

    errors = {}

    input_json = request.get_json(force=True)
    idx = input_json['id']
    date_str = input_json['datetime']
    if not task.validate_datetime(date_str):
        errors[idx] = 'task not made'
    else:
        print(f'creating new job for id {idx}')
        
        if not task.create_job(idx, date_str):
            return "didnt work" # bubble up error
    return "Hello, World!"