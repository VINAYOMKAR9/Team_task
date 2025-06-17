from flask import Blueprint, render_template, request, redirect, url_for, flash , jsonify

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods='GET')
def login():

        # Add login form handling logic here
        return jsonify(msg = f' "Login logic not implemented yet", "info"')
    # return jsonify(msg = 'abdo')
