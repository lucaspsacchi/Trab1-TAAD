#!flask/bin/python
from flask import Flask, jsonify, abort
from datetime import datetime
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = [
    {
        'id': 1,
        'timestamp': u'Buy groceries'
    }
]

# GET exibe lista de todas as tasks
def get_infos():
    return jsonify({'infos': tasks})

def get_info(info):
    task = [task for task in tasks if task['id'] == info]
    if len(task) == 0:
        abort(404)
    return jsonify({'info': task[0]})

def create_info():
    task = {
        'id': tasks[-1]['id'] + 1,
        'timestamp': datetime.now()
    }
    tasks.append(task)
    return jsonify({'info': task}), 201


api.add_resource(get_infos, 'GET_INFO')
api.add_resource(get_info, 'GET_INFO/<int:info>')
api.add_resource(create_info, 'POST_INFO')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
