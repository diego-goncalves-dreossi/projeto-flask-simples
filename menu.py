from flask import Flask, render_template

# Recomendação da documentação do Flask para de chamada do site
app = Flask(__name__)

# Criar a primeira página do site (qualquer página no flask)
# route -> caminhos depois do domínio
# @app.route()
# função -> o que você quer exibir naquela página

# Decorator é uma linha que atribui nova funcionalidade a uma função em baixo dela. Nesse caso a função vai ser exibida na página inicial
# Exibido em servidor local
@app.route("/")
def paginaInicial():
    return render_template("html/pagina_inicial.html")


@app.route("/contatos")
def contatos():
    return render_template("html/contatos.html")

# <> torna dinamico
@app.route("/usuarios/<nome>")
def usuarios(nome):
    return render_template("html/usuario.html", nome=nome)

# Colocar o site no ar
# Executa o projeto quando estivermos rodando o código diratemente, impossibilitando que se rode caso se importe para outro arquivo
if __name__ == "__main__":
    app.run(debug=True) 
# degug=True vai permitir que as edições feitas possam ser vistas no site em vez de ter que reiniciar o projeto