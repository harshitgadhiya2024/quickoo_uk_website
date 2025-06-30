from flask import Flask, render_template, request, flash, redirect, url_for
import os
from datetime import datetime
import uuid
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', str(uuid.uuid4()))

# Configuration
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

client = MongoClient("mongodb+srv://harshitgadhiya8980:harshitgadhiya8980@cluster0.xradpzd.mongodb.net/")

@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/about')
def about():
    return render_template('about2.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # In production, you would send this to an email service
        mapping_dict = {"name": name, "email": email, "phone": phone, "message": message}
        db = client["quickoouk"]
        coll = db["contact_forms"]
        coll.insert_one(mapping_dict)
        # For now, we'll just flash a success message
        flash('Thank you for contacting us! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact2.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)