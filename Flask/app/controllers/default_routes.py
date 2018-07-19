from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
from app import app, db
from app.models.forms import PecaSchema, PecaForm
from app.models.tables import Peca


peca_schema = PecaSchema()
pecas_schema = PecaSchema(many=True)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

'''
@app.route("/cadastrarj", methods=['GET','POST'])
def cadastrar():
    nome = request.json['nome']
    desc = request.json['desc']
    valorC = request.json['valorC']
    valorV = request.json['valorV']
    qtde = request.json['qtde']

    if nome and desc and valorC and valorV and qtde:
        peca = Peca(nome, desc, valorC, valorV, qtde)
        db.session.add(peca)
        db.session.commit()
        return '<h1>Funcionando</H1>'

    form_peca = PecaForm()
    return render_template("peca/cadastrar-peca.html", form_peca=form_peca)

'''
@app.route("/novo", methods=['GET','POST'])
def addPeca():
    nome = request.json['nome']
    desc = request.json['desc']
    valorC = request.json['valorC']
    valorV = request.json['valorV']
    qtde = request.json['qtde']

    if nome and desc and valorC and valorV and qtde:
        peca = Peca(nome, desc, valorC, valorV, qtde)
        db.session.add(peca)
        db.session.commit()
        return peca_schema.jsonify(peca)


@app.route("/peca", methods=['GET'])
def get_peca():
    all_pecas = Peca.query.all()
    result = pecas_schema.dump(all_pecas)
    return jsonify(result.data)

@app.route("/peca/<id>", methods=['GET'])
def peca_detail(id):
    peca = Peca.query.get(id)
    return peca_schema.jsonify(peca)

@app.route("/peca/<id>", methods=['PUT'])
def peca_update(id):
    peca = Peca.query.get(id)
    nome = request.json['nome']
    desc = request.json['desc']
    valorC = request.json['valorC']
    valorV = request.json['valorV']
    qtde = request.json['qtde']

    peca.nome = nome
    peca.descricao = desc
    peca.valorCompra = valorC
    peca.valorVenda = valorV
    peca.qtde = qtde

    db.session.commit()
    return peca_schema.jsonify(peca)

@app.route("/peca/<id>", methods=['DELETE'])
def peca_delete(id):
    peca = Peca.query.get(id)
    db.session.delete(peca)
    db.session.commit()
    return "<h1>Excluído com sucesso</h1>"

@app.route("/novapeca", methods=['GET', 'POST'])
def novaPeca():
    if request.method == "POST":
        nome = request.form.get('nome')
        desc = request.form.get('descricao')
        valorC = request.form.get('valorCompra')
        valorV = request.form.get('valorVenda')
        qtde = request.form.get('qtde')

        if nome and desc and valorC and valorV and qtde:
            peca = Peca(nome, desc, valorC, valorV, qtde)
            db.session.add(peca)
            db.session.commit()
            flash("Peca cadastrada com sucesso!")
            return redirect(url_for('listar_peca'))

    form_peca = PecaForm()
    return render_template("peca/cadastrar-peca.html", form_peca=form_peca)


@app.route("/listar-peca", methods=["GET", "POST"])
def listar_peca():
    peca = db.session.query(Peca).all()
    return render_template("peca/listar-peca.html", peca = peca)

@app.route("/editar-peca/<int:id>", methods=["GET","POST"])
@app.route('/editar-peca', methods=['POST'])
def atualizar_peca(id):
    if id != None and request.method == "GET":
        peca = Peca.query.filter_by(id=id).first()
        form_peca = PecaForm()
        return render_template('peca/atualizar-peca.html', form_peca=form_peca, peca=peca)
    elif request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valorC = request.form.get("valorCompra")
        valorV = request.form.get("valorVenda")
        qtde = request.form.get("qtde")



        if nome and descricao and valorC and valorV and qtde:
            peca = Peca.query.filter_by(id=id).first()
            peca.nome = nome
            peca.descricao = descricao
            peca.valorCompra = valorC
            peca.valorVenda = valorV
            peca.qtde = qtde
            db.session.commit()
            flash("Alterações registradas com sucesso!")
        return redirect(url_for('listar_peca'))

@app.route("/apaga-peca/<id>", methods=['GET'])
def apaga_peca(id):
    peca = Peca.query.get(id)
    db.session.delete(peca)
    db.session.commit()
    flash("Peça excluida com sucesso!")
    return redirect(url_for('listar_peca'))