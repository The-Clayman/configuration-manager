__version__ = "1.0.0"

import os
from os import listdir
from flask import Flask, Response, send_from_directory

# env param after resolve
env_params = {}

app = Flask(__name__)


# Resolve param from env, with fallback to default values
@app.before_first_request
def resolve_param_from_env():
    global env_params

    # resolve env params, with default fallbacks
    env_params["data_folder_location"] = os.getenv("DATA_FOLDER", "/Data")

    app.logger.warning("Env param loaded, with fall back to defaults")
    app.logger.warning(env_params)


# Wraps message in json response body, with status
def wrap_message_response_in_json(message, status):
    response = Response(response=f"{{ \"message\" :\"{message}\" }}", status=status)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/configuration_manager/v1/version", methods=['GET'])
def get_version():
    return wrap_message_response_in_json(f"Configuration Manager, version:[{__version__}]", 200)


# Returns a list of files exist under data folder
@app.route("/configuration_manager/v1/files", methods=['GET'])
def get_files():
    path = env_params["data_folder_location"]
    return wrap_message_response_in_json(f"Available files: {listdir(path)}", 200)


# Returns file content by file_name
@app.route("/configuration_manager/v1/file/<string:file_name>", methods=['GET'])
def get_file(file_name):
    path = env_params["data_folder_location"]
    return send_from_directory(path, file_name)

if __name__=="__main__":
    app.run()
