import os
from dotenv import load_dotenv

# load .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import TableObject

app = create_app(config_name=os.getenv('FLASK_CONFIG', 'default'))
migrate = Migrate(app=app, db=db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, TableObject=TableObject)


@app.cli.command()
def deploy():
    # migrate database to latest revision
    upgrade()
