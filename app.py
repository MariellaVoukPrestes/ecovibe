from flask import Flask, render_template


app= Flask(__name__)

#primeira pag
#route-> ecovibe.com/Produtos -> Produtos é o route,ou seja, é o caminho que define a pagina
@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html")

@app.route("/Sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/Informações")
def info():
    return render_template("info.html")

@app.route("/aviso")
def aviso():
    return render_template("aviso.html")

#colca no ar bb
if __name__ == "__main__":
    app.run(debug=True)


#servidor heroku

