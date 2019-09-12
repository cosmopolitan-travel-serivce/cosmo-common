import dotenv
import os


def load_config_file(file_path: str):
    dotenv.load_dotenv(dotenv_path=file_path)


def get_config(name: str, default=None):
    return os.environ.get(name, default)
