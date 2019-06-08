#!flask/bin/python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'timestamp': u'Buy groceries'
    }
]

# interface = {
#   '/GET_INFO': u'Recupera todas as informações armazenadas',
#   '/GET_INFO/id_info': u'Recupera a informação com o id passado'
# }

# @app.route('/HOME', methods=['GET'])
# def interface():
#   return jsonify({'Menu': interface});

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
    # if not request.json or not 'title' in request.json:
    #     abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'timestamp': datetime.now()
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


#!flask/bin/python
# from flask import Flask, jsonify, abort
# from datetime import datetime
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# tasks = [
#     {
#         'id': 1,
#         'timestamp': u'Buy groceries'
#     }
# ]

# # GET exibe lista de todas as tasks
# def get_infos():
#     return jsonify({'infos': tasks})

# def get_info(info):
#     task = [task for task in tasks if task['id'] == info]
#     if len(task) == 0:
#         abort(404)
#     return jsonify({'info': task[0]})

# def create_info():
#     task = {
#         'id': tasks[-1]['id'] + 1,
#         'timestamp': datetime.now()
#     }
#     tasks.append(task)
#     return jsonify({'info': task}), 201


# api.add_resource(get_infos, 'GET_INFO')
# api.add_resource(get_info, 'GET_INFO/<int:info>')
# api.add_resource(create_info, 'POST_INFO')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
