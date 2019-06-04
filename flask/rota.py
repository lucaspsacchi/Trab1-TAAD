from flask import Flask, request, render_template
app = Flask(__name__) # Nome da aplicação

@app.route('/teste') # Rota raiz
def teste():
    arg = request.args.get("Argumento");
    return render_template("/", arg), 200

app.run(use_reloader=True)
