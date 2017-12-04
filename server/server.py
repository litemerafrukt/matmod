"""
Small flask server used in matmod
"""
import time
from flask import Flask, render_template, send_file, jsonify
from uppgift1.plot_malmo import main as generate_malmo_files

# app = Flask(__name__)
app = Flask(
    __name__,
    static_folder="../client/build/static",
    template_folder="../client/build")


@app.route('/api/assignment/1/malmonow-generate')
def malmonow_genereate():
    generate_malmo_files()
    return jsonify({"result": "ok", "time": int(time.time()) * 1000})


@app.route('/api/assignment/1/malmonow-image', methods=['GET'])
def malmonow_image():
    return send_file('../malmonow.png', mimetype='image/png')


@app.route('/api/assignment/1/malmonow-text', methods=['GET'])
def malmonow_text():
    return send_file('../malmonow.txt', mimetype='text/plain')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
