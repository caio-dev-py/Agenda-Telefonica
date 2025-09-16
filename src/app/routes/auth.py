from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from src.app.forms import LoginForm, CadastroForm
from src.app.models import db, Usuarios
from werkzeug.security import generate_password_hash, check_password_hash


auth_route = Blueprint("auth", __name__, url_prefix="/auth")


@auth_route.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = generate_password_hash(form.senha.data)
        
        usuario_existente = Usuarios.query.filter_by(email=email).first()
        
        if not usuario_existente:
            usuario = Usuarios(nome=nome, email=email, senha=senha)
            
            db.session.add(usuario)
            db.session.commit()
            
            flash("Usuário cadastrado com sucesso.", "success")
            
            return redirect(url_for("auth.login"))
        flash ("Usuário já existe.", "warning")
        return redirect(url_for("auth.login"))
    
    return render_template("cadastro.html", form=form)

@auth_route.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        usuario = Usuarios.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario)
            
            flash ("Usuário logado com sucesso.", "success")
            return redirect(url_for("home.home"))
        flash ("Credenciais incorretas.", "danger")
        return redirect(url_for("auth.login"))
    return render_template("login.html", form=form)


@auth_route.route("/logout")
def logout():
    logout_user()
    
    flash ("Usuário deslogado.", "success")
    return redirect(url_for("auth.login"))