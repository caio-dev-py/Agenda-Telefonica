from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class CadastroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(message="O nome não pode estar vazio.")])
    email = StringField("E-mail", validators=[DataRequired(message="O e-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                               Length(min=8, message="A senha deve ter pelo menos 8 caracteres.")])
    conf_senha = PasswordField("Confirmar Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                                                Length(min=8, message="A senha deve ter pelo menos 8 caracteres."),
                                                                EqualTo("senha", message="As senhas não coincidem.")])
    cadastrar = SubmitField("Cadastrar")
    
class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(message="O e-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                               Length(min=8, message="A senha deve ter pelo menos 8 caracteres.")])
    login = SubmitField("Login")
    
class AgendaForm(FlaskForm):
    nome = StringField("Nome Contato", validators=[DataRequired(message="Nome vazio.")])
    telefone = StringField("Telefone", validators=[DataRequired(message="Telefone vazio.")])
    email = StringField("E-mail", validators=[DataRequired(message="E-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    salvar = SubmitField("Salvar")
    
class DeletarForm(FlaskForm):
    deletar = SubmitField("Deletar")