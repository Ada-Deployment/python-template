from flask import Flask, app, jsonify

application = app = Flask(__name__)


@app.route('/', methods=['GET',
                         'POST'])  #landing page redirects to the sign in page
def index():
    return jsonify("  Testing    new     blue/green deployment")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
