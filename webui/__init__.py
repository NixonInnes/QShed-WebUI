import os
import logging

from .app import create_app
from .app.html.sidebar import Sidebar


logger = logging.getLogger(__name__)


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    try:
        from dotenv import load_dotenv

        load_dotenv(dotenv_path)
        logger.info("Loaded environment file: {dotenv_path}")
    except Exception as e:
        logger.warn(f"{e}\nUnable to load environment file: {dotenv_path}")


app = create_app()

app.jinja_env.globals["sidebar"] = Sidebar()


@app.shell_context_processor
def make_shell_context():
    return dict()