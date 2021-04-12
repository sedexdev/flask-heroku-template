from flask import Flask
from core.views import core_blueprint
from users.views import user_blueprint

app = Flask(__name__)

app.register_blueprint(core_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
