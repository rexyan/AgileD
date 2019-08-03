from src import app

if __name__ == "__main__":
    RUN_MODEL = app.config["RUN_MODEL"]
    server = app.run(**RUN_MODEL)
