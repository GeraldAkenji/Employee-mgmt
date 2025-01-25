from flask import Flask
from app.routes import main
from app.models import db

app = Flask(__name__)
app.config.from_object('app.config.Config')

db.init_app(app)

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
