import os  # Import the os module
from main import app, db

app.app_context().push()
app.config['SQLALCHEMY_INSTANCE_FOLDER'] = os.path.join(os.getcwd(), 'instance')
db.create_all()
