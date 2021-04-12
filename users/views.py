from flask import Blueprint, render_template, request

user_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template(
        'login.html',
        title='Login')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass
    return render_template(
        'register.html',
        title='Register')


@user_blueprint.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        pass
    return render_template(
        'reset_pw.html',
        title='Reset')
