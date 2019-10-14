# imported modules
from flask import Flask, render_template, request, send_file, send_from_directory
from werkzeug import secure_filename
from compare_files import compare_files
import os
import rdflib

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# to prevent caching of previous result
file_counter = 0
app.config["allowed_file_extensions"] = ["csv", "xls"]
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
file_name = ""


class API:

    def __init__(self):
        app.run(host="127.0.0.1", port="5000", threaded=True, debug=True)

    @app.route("/", methods=["GET", "POST"])
    def get_files():
            if request.method == "POST":
                file_1 = request.files['file_1']
                filename_1 = secure_filename(file_1.filename)
                file_path_1 = os.path.join(app.config['UPLOAD_FOLDER'], filename_1)
                file_1.save(file_path_1)
                file_2 = request.files['file_2']
                filename_2 = secure_filename(file_1.filename)
                file_path_2 = os.path.join(app.config['UPLOAD_FOLDER'], filename_2)
                file_2.save(file_path_2)
                return compare_files(file_path_1, file_path_2)
            else:
                return render_template("file_upload.html")


if __name__ == "__main__":
    # start api
    API()