from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from datetime import datetime
import uuid
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', str(uuid.uuid4()))

# Configuration
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'info@quickoo.co.uk')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'Quickoo@#2025')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME', 'info@quickoo.co.uk')

mail = Mail(app)

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

        # Save to database
        mapping_dict = {"name": name, "email": email, "phone": phone, "message": message}
        db = client["quickoouk"]
        coll = db["contact_forms"]
        coll.insert_one(mapping_dict)

        # Send email notification
        try:
#             msg = Message(
#                 subject=f'Quickoo Website: Contact Form {name}',
#                 recipients=['guest.quickoo@gmail.com'],
#                 reply_to=email
#             )

#             # Email body
#             msg.body = f"""
# Quickoo Website: Contact Form Submission

# Name: {name}
# Email: {email}
# Phone: {phone}

# Message:
# {message}

# ---
# This email was sent from the Quickoo UK website contact form.
#             """

#             # HTML version of the email (optional, but looks better)
#             msg.html = f"""
# <html>
# <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
#     <h2 style="color: #2c3e50;">Quickoo Website: Contact Form Submission</h2>

#     <table style="width: 100%; max-width: 600px; border-collapse: collapse;">
#         <tr>
#             <td style="padding: 10px; background-color: #f8f9fa; font-weight: bold; width: 100px;">Name:</td>
#             <td style="padding: 10px; background-color: #ffffff;">{name}</td>
#         </tr>
#         <tr>
#             <td style="padding: 10px; background-color: #f8f9fa; font-weight: bold;">Email:</td>
#             <td style="padding: 10px; background-color: #ffffff;"><a href="mailto:{email}">{email}</a></td>
#         </tr>
#         <tr>
#             <td style="padding: 10px; background-color: #f8f9fa; font-weight: bold;">Phone:</td>
#             <td style="padding: 10px; background-color: #ffffff;">{phone}</td>
#         </tr>
#     </table>

#     <div style="margin-top: 20px; padding: 15px; background-color: #f8f9fa; border-left: 4px solid #2c3e50;">
#         <h3 style="margin-top: 0;">Message:</h3>
#         <p style="white-space: pre-wrap;">{message}</p>
#     </div>

#     <hr style="margin-top: 30px; border: none; border-top: 1px solid #ddd;">
#     <p style="font-size: 12px; color: #666;">This email was sent from the Quickoo UK website contact form.</p>
# </body>
# </html>
#             """

#             mail.send(msg)
            flash('Thank you for contacting us! We will get back to you soon.', 'success')
        except Exception as e:
            # Log the error but still show success to user
            # print(f"Error sending email: {str(e)}")
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