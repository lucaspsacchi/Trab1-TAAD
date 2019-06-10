#!flask/bin/python
from flask import Flask, jsonify, abort, request
from datetime import datetime

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
    data = json.dumps(request.body)
    print("AAAAAAAAAAAA")
    print(str(request))
    # if not request.json or not 'title' in request.json:
    #     abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'timestamp': datetime.now(),
        'nome': data['nome'],
        'id_container': data['id_container'],
        'id_naosei': data['id'] # NAO SEI
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
