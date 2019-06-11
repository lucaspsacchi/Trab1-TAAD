#!flask/bin/python
from flask import Flask, jsonify, abort, request
from datetime import datetime
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'id_container': '8eb5f22773cf',
        'timestamp': 'Mon, 10 Jun 2019 22:33:50 GMT',
        'nome': 'cocky_brown',
        'cpu_usage': '1056052634',
        'memory_stats': '15421440'
    }
]

# GET exibe lista de todas as tasks
@app.route('/GET_INFO', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/GET_INFO/<int:info>', methods=['GET'])
def get_task(info):
    task = [task for task in tasks if task['id'] == info]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/POST_INFO', methods=['POST'])
def create_task():

    r = json.dumps(request.get_json())

    task = {}
    task["id"] = tasks[-1]['id'] + 1
    task["timestamp"] = datetime.now()
    task["nome"] = r['nome']
    task["id_container"] = r['id_container']
    # task['cpu_usage'] = r['cpu_usage']
    # task['memory_stats'] = r['memory_stats']

    tasks.append(task)
    return jsonify(task)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
