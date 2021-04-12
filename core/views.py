from flask import Blueprint, render_template, request

core_blueprint = Blueprint(
    'core',
    __name__,
    template_folder='templates')


@core_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    return render_template(
        'index.html',
        title='Index')
