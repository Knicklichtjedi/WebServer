from flask import Flask, send_from_directory, jsonify, Response
import FileHandler

app = Flask(__name__,
            static_url_path='',
            static_folder='./frontend/dist')


@app.route("/")
def root():
    """
    Default route serving Vue distributions
    """
    return send_from_directory("./frontend/dist/", "index.html")


@app.route("/data")
def get_dataframe_data() -> Response:
    """
    Data route to serve raw data in json format
    :return: Response object with raw data in json format
    """
    dataframe = FileHandler.get_df()
    dataframe_as_json = FileHandler.df_to_json(dataframe)
    return jsonify(dataframe_as_json)


if __name__ == "__main__":
    # server startup
    app.run()
