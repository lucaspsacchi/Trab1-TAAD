from flask import Flask
app = Flask(__name__) # Nome da aplicação

@app.route('/<arg>') # Rota raiz
def hello_world(arg):
  if not arg:
    return "Hello World"
  else:
    return 'Hello, World!' . format(arg) . 200 # 200 representa o ok
