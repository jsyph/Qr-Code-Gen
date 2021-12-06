from create_qr import QrCodeImg
from flask import Flask, render_template, send_from_directory, request, url_for
from form import QrCodeData
from dotenv import load_dotenv
import os
import pathlib

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("PRIVATE_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    form = QrCodeData()
    if request.method == "POST":
        if form.validate_on_submit():
            if len(os.listdir("static/temp")) > 0:
                [os.remove(f"static/temp/{file}") for file in os.listdir("static/temp")]
            data_text = form.data_input.data
            qr_code_img = QrCodeImg(data_text)
            path_to_png = f"../{qr_code_img.file_path}"
            return render_template("index.html", form=form, image_created=True, image_name=path_to_png)

    return render_template("index.html", form=form, image_created=False)


@app.route("/send_file", methods=["POST"])
def send_qr_code():
    path_to_image = request.args.get("path").split("..")[1]
    file_name = pathlib.Path(path_to_image).name
    return send_from_directory(directory="static/temp", path=file_name, as_attachment=True)


if "__main__" == __name__:
    app.run(debug=True)
