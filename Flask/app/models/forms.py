from flask import  Flask
from flask_marshmallow import Marshmallow
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

ma = Marshmallow()

class PecaSchema(ma.Schema):
    class Meta:
        fields = ('nome', 'descricao', 'valorCompra', 'valorVenda', 'qtde', 'id')

class PecaForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    valorCompra = StringField("valorCompra", validators=[DataRequired()])
    valorVenda = StringField("valorVenda", validators=[DataRequired()])
    descricao = StringField("descricao", validators=[DataRequired()])
    qtde = StringField("qtde", validators=[DataRequired()])






