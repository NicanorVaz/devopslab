from flask import Flask
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)

csrf = CsrfProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run()