import base64
import io
from flask import Flask, render_template, request, url_for, session, redirect
import os
import uuid
from PIL import Image as PILImage
from predict import predict_disease
from disease_info import get_disease_info, DISEASE_INFO

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'skin-disease-chatbot-secret-key-2024')

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static')
# For cloud/serverless environments like Vercel, we might need /tmp
if os.environ.get('VERCEL'):
    UPLOAD_FOLDER = '/tmp'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def is_valid_image(filepath):
    """Use Pillow to verify the file is a valid image, regardless of extension."""
    try:
        with open(filepath, 'rb') as f:
            with PILImage.open(f) as img:
                img.verify()
        return True
    except Exception:
        return False


@app.route('/health')
def health():
    return {"status": "online", "message": "Skin Disease Chatbot is running"}, 200


@app.route('/')
def home():
    # Get list of diseases for the gallery (exclude "Uncertain Prediction")
    diseases = {k: v for k, v in DISEASE_INFO.items() if k != "Uncertain Prediction"}
    return render_template('index.html', diseases=diseases)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return redirect(url_for('home'))

    if 'file' not in request.files:
        return render_template('result.html', disease='Error', confidence=0, risk_level='-',
                              image_url=None, prob_labels=[], prob_values=[], error='No file uploaded.',
                              disease_info=get_disease_info('Uncertain Prediction'))

    file = request.files['file']
    if file.filename == '':
        return render_template('result.html', disease='Error', confidence=0, risk_level='-',
                               image_url=None, prob_labels=[], prob_values=[], error='No file selected.',
                               disease_info=get_disease_info('Uncertain Prediction'))

    # No extension restriction — save first, then validate with Pillow

    # Unique filename so uploads don't overwrite each other
    original_name = file.filename or 'upload'
    ext = original_name.rsplit('.', 1)[-1].lower() if '.' in original_name else 'jpg'
    safe_name = f"{uuid.uuid4().hex}.{ext}"
    
    # Use absolute path to avoid cwd issues
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], safe_name)
    file.save(filepath)

    # Validate that the saved file is actually a readable image
    try:
        if not is_valid_image(filepath):
            if os.path.exists(filepath):
                os.remove(filepath)
            return render_template('result.html', disease='Error', confidence=0, risk_level='--',
                                   image_url=None, prob_labels=[], prob_values=[],
                                   error='The uploaded file is not a valid image. Please upload any common image format (JPG, PNG, WEBP, HEIC, TIFF, etc.).',
                                   disease_info=get_disease_info('Uncertain Prediction'))
        
        # For Online mode: Encode image to Base64 for the results page
        with open(filepath, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            image_url = f"data:image/{ext};base64,{encoded_string}"
            
    except Exception as e:
        return render_template('result.html', disease='Error', confidence=0, risk_level='--',
                               image_url=None, prob_labels=[], prob_values=[], error=f"Validation failed: {str(e)}",
                               disease_info=get_disease_info('Uncertain Prediction'))

    try:
        disease, confidence, probability_data = predict_disease(filepath)
    except Exception as e:
        # Avoid charmap issues in error reporting
        error_msg = str(e).encode('ascii', 'ignore').decode('ascii')
        return render_template('result.html', disease='Error', confidence=0, risk_level='--',
                               image_url=image_url, prob_labels=[], prob_values=[], error=error_msg,
                               disease_info=get_disease_info('Uncertain Prediction'))

    # Confidence Safety Check
    if confidence < 45:
        disease = "Uncertain Prediction"

    # Risk Score from symptom questions
    risk_score = 0
    if request.form.get('bleeding') == 'yes':
        risk_score += 2
    if request.form.get('growth') == 'yes':
        risk_score += 2
    if request.form.get('itching') == 'yes':
        risk_score += 1
    if request.form.get('duration') == 'weeks':
        risk_score += 1
    elif request.form.get('duration') == 'months':
        risk_score += 2

    if risk_score >= 4:
        risk_level = "High Risk"
    elif risk_score >= 2:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    prob_labels = list(probability_data.keys())
    prob_values = list(probability_data.values())

    # Get disease information
    disease_info = get_disease_info(disease)

    # Store in session history
    try:
        if 'history' not in session:
            session['history'] = []

        session['history'].append({
            'disease': disease,
            'confidence': confidence,
            'risk_level': risk_level,
            'image_url': image_url,
        })
        # Keep only last 10 analyses
        session['history'] = session['history'][-10:]
        session.modified = True
    except Exception:
        pass # History failure shouldn't crash the result

    # Cleanup temporary file after prediction
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception:
        pass

    return render_template(
        'result.html',
        disease=disease,
        confidence=confidence,
        risk_level=risk_level,
        image_url=image_url,
        prob_labels=prob_labels,
        prob_values=prob_values,
        error=None,
        disease_info=disease_info,
    )


@app.route('/history')
def history():
    analyses = session.get('history', [])
    return render_template('history.html', analyses=analyses)


if __name__ == '__main__':
    # Use PORT from environment variable (common for cloud platforms)
    port = int(os.environ.get('PORT', 5000))
    # host='0.0.0.0' allows external connections
    app.run(host='0.0.0.0', port=port, debug=False)