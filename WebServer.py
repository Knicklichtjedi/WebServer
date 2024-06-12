from flask import Flask, send_from_directory

app = Flask(__name__,
            static_url_path='',
            static_folder='./frontend/dist')


@app.route("/")
def root():
    """
    Default route serving Vue distributions
    """
    return send_from_directory("./frontend/dist/", "index.html")


if __name__ == "__main__":
    # server startup
    app.run()
