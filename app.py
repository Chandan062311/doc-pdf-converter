import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash
from werkzeug.utils import secure_filename
from docx2pdf import convert as docx2pdf_convert
from pdf2docx import Converter

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key'  # Replace with a random secret key

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser may submit an empty part
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            # Determine conversion type
            ext = filename.rsplit('.', 1)[1].lower()
            if ext == 'docx':
                # Convert DOCX to PDF
                output_filename = filename.rsplit('.', 1)[0] + '.pdf'
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                docx2pdf_convert(input_path, output_path)
            elif ext == 'pdf':
                # Convert PDF to DOCX
                output_filename = filename.rsplit('.', 1)[0] + '.docx'
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                cv = Converter(input_path)
                cv.convert(output_path, start=0, end=None)
                cv.close()
            else:
                flash('Unsupported file type.')
                return redirect(request.url)

            return send_from_directory(app.config['UPLOAD_FOLDER'], output_filename, as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)