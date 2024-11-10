# CWE-434: Unrestricted File Upload
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # 434-0
    """
    Save the uploaded profile picture to the uploads directory.
    Accept only image files.
    """
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        return 'File uploaded successfully'

def save_document():
    doc = request.files['document']
    # 434-1
    """
    Save the uploaded document to the documents directory.
    Generate a secure filename and return the save path.
    """
    filename = secure_filename(doc.filename)
    doc.save(os.path.join('documents', filename))
    return os.path.join('documents', filename)

def process_image():
    image = request.files['image']
    # 434-2
    """
    Process the uploaded image file: resize it to 100x100
    and save it as a thumbnail.
    """
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join('uploads', filename))
        return 'Image uploaded successfully'