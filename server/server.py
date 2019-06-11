#!flask/bin/python
from flask import Flask, jsonify, abort, request
from datetime import datetime
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'timestamp': u'Buy groceries'
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
    print("AQUI" + str(request))
    r = request.get_json()

    task = {}
    task["id"] = tasks[-1]['id'] + 1
    task["timestamp"] = datetime.now()
    task["nome"] = r.data['nome']
    task["id_container"] = r.data['id_container']
    task["id_naosei"] = r.data['id']
    tasks.append(task)
    return jsonify(task)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
