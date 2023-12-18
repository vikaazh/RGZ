from config import db, app, login_manager
from route.fetch import fetch

app.config['SECRET_KEY'] = 'test for testing test'

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(fetch)


if __name__ == "__main__":
    app.run(debug=True)
