from flask import Flask, render_template,url_for, redirect,request

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobremi")
def sobremi():
    return render_template("sobremi.html")

@app.route("/portafolio")
def portafolio():
    return render_template("portafolio.html")

@app.route("/contacto")
def contacto():
    return render_template("/contacto.html")

@app.route("/formulario", methods=["POST"])
def formulario():
        nom = request.form['Nombre']
        mail = request.form['Email']
        return render_template("mensaje.html", nom=nom, mail=mail)
  

if __name__ == "__main__": 
    app.run()

