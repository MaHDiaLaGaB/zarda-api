from sql.db import db
from project import create_app

app = create_app()
with app.test_request_context():
    db.init_app(app)
    db.create_all()