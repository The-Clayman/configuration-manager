__version__ = "1.0.0"

from flask import Flask, Response

app = Flask(__name__)

# wrap message in json body
def wrap_message_response_in_json(message, status):
    response = Response(response=f"{{ \"message\" :\"{message}\" }}", status=status)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/configuration_manager/v1/version", methods=['GET'])
def get_version():
    return wrap_message_response_in_json(f"Configuration Manager, version:[{__version__}]", 200)

if __name__=="__main__":
    app.run()