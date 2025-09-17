from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from src.app.forms import AgendaForm
from src.app.models import db, Contatos
from app.utils.functions import valida_numero, admin_required

user_route = Blueprint("user", __name__)

@user_route.route("/agenda")
@login_required
def agenda():
    form = AgendaForm()
    contatos = Contatos.query.filter_by(usuario_id=current_user.id).all()
    
    return render_template("agenda.html", form=form, contatos=contatos)

@user_route.route("/adicionar_contato", methods=["GET", "POST"])
@login_required
def adicionar_contato():
    form = AgendaForm()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        telefone = form.telefone.data
        
        if not valida_numero(telefone):
            flash ("Formato de telefone inválido", "danger")
            return redirect(url_for("user.adicionar_contato"))
        
        contato_existente = Contatos.query.filter_by(email=email).first()
        
        if not contato_existente:
            contato = Contatos(usuario_id=current_user.id, nome=nome, email=email, telefone=telefone)
            
            db.session.add(contato)
            db.session.commit()
            
            flash("Contato salvo com sucesso.", "success")
            return redirect(url_for("user.agenda"))
        flash ("Já existe um usuário com esse e-mail.", "warning")
        return redirect(url_for("user.agenda"))
    return render_template("adicionar_contato.html", form=form)