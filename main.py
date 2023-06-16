from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    # Check if an image file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    # Call your OCR script to extract text from the image file
    # extracted_text = your_ocr_script.extract_text(file)
    extracted_text = "YESSSSSSIR"


    # Return the extracted text as a JSON response
    return jsonify({'text': extracted_text})


@app.route('/ocr2', methods=['GET'])
def ocr2():
    extracted_text = "GOTTOMEE"
    return jsonify({'text': extracted_text})

if __name__ == '__main__':
  app.run(port=5000)
