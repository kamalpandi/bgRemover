from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method =='POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            # Open an image from a file stream
            input_image = Image.open(file.stream)
            # Remove background and apply post-processing to the mask
            output_image = remove(input_image, post_process_mask=True)
            # Create a BytesIO object to hold the image data in memory
            img_io = BytesIO()
            # Save the image to the BytesIO object in PNG format
            output_image.save(img_io,'PNG')
            # Move the file pointer to the beginning of the BytesIO object
            img_io.seek(0)
            # return send_file(img_io, mimetype='image/png')  # Change download in separatre browser tab
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_rmbg.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)