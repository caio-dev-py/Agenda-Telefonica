from flask import Blueprint, render_template
from src.app.forms import AgendaForm

user_route = Blueprint("user", __name__)

@user_route.route("/agenda")
def agenda():
    form = AgendaForm()
    return render_template("agenda.html", form=form)