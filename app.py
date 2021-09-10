from flask import Flask
import random
from flask import request
from pathlib import Path
import os
from flask import jsonify
from werkzeug.utils import secure_filename

from diabete_predict import predict2

app = Flask(__name__)


#configuration de l'application pour lui specifier le repertoire où stocker les fichiers uploadés
app.config['UPLOAD_FOLDER'] = Path('./uploads')

html_template = """
<!doctype html>
<title>Upload New file </title>
<h1>CSV file </h1>
<form action="" method='post' enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type='submit' value='Soumettre'></p>    
</form>
"""


@app.route("/")
def hello_world():
    return "Hello, World! from DIT"

@app.route("/predict", methods = ['GET', 'POST'])
def predict_main():
    if request.method == 'POST':
        file = request.files['file']#recuperation du fichier uploadé
        filename = secure_filename(file.filename)#recuperation du nom du fichier uploadé
        full_path_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)#Chemin complet vers notre fichier uploadé
        file.save(full_path_file)#Enregistrement dans le repertoire d'upload
        predictions = predict2(full_path_file)
        return jsonify(str(predictions))
    else:
        return html_template
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)