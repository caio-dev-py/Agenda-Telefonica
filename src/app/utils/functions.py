# FUNÇÃO PARA VALIDAR NÚMEROS

from phonenumbers import is_valid_number, parse

def valida_numero(telefone: str, regiao: str="BR") -> bool:
    try:
        numero = parse(telefone, regiao)
        return is_valid_number(numero)
    except:
        return False
    
# FUNÇÃO PARA PROTEGER A ROTA DO ADMIN

from functools import wraps
from flask import flash, redirect, url_for
from flask_login import login_required, current_user

def admin_required(funcao_original):
    @wraps(funcao_original)
    @login_required
    def funcao_decorada(*args, **kwargs):
        if current_user.is_authenticated and current_user.role != "admin":
            flash ("O usuário não tem permissão para acessar essa página.", "warning")
            return redirect(url_for("home.home"))
        return funcao_original(*args, **kwargs)
    return funcao_decorada