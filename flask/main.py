#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    }
]

interface = {
  '/GET_INFO': u'Recupera todas as informações armazenadas',
  '/GET_INFO/id_info': u'Recupera a informação com o id passado'
}

@app.route('/HOME', methods=['GET'])
def interface():
  return jsonify({'Menu': interface});

# GET exibe lista de todas as tasks
@app.route('/GET_INFO', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/GET_INFO/<int:info>', methods=['GET'])
def get_task(info):
    task = [task for task in tasks if task['id'] == info]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/POST_INFO', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
