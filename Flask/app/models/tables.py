from app import db

class Peca(db.Model):
    #define o nome da tabela no bd
    __tablename__ = "pecas"

    #Todos os atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(60))
    valorVenda = db.Column(db.Float)
    valorCompra = db.Column(db.Float)
    qtde = db.Column(db.Integer)

    #define os tributos de inicializacao
    def __init__(self, nome, descricao, valorVenda, valorCompra, qtde):
        self.nome = nome
        self.descricao = descricao
        self.valorVenda = valorVenda
        self.valorCompra = valorCompra
        self.qtde = qtde

    #retorna dados da peca
    def __repr__(self):
        return "<peca %r>" % self.nome
