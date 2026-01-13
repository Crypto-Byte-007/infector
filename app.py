from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files.get("file")
        if f:
            filename = f.filename
            f.save(os.path.join(UPLOAD_FOLDER, filename))
            return "Uploaded."

    return '''
    <h2>Upload your file</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit">
    </form>
    '''

@app.route("/uploads/shell.py")
def shell():
    return "FLAG: NULLCTF{Upl0oad_F1lters_are_A_1ie}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
