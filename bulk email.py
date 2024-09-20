from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'fe1d025e3ad663ecf992d47c6f2df188bbb55933562550287a4ab9aafb0701c3'  # Necessary for flashing messages

# Route to render the bulk email page
@app.route('/')
def index():
    return render_template('bulk_email.html')

# Route to handle form submission
@app.route('/send_bulk_email', methods=["GET",'POST'])
def send_bulk_email():
    try:
        # Get form data
        emails = request.form['emails']
        subject = request.form['subject']
        message_content = request.form['message']

        # Split the emails by comma and trim spaces
        email_list = [email.strip() for email in emails.split(',')]

        # Email credentials
        sender_email = 'kghvvh135@gmail.com'
        sender_password = 'zozw nbbi yags dfdp'

        # SMTP server configuration (using Gmail's SMTP server)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Create an email session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)

            # Create the email
            for recipient_email in email_list:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject

                # Attach the message body
                msg.attach(MIMEText(message_content, 'plain'))

                # Send the email
                server.sendmail(sender_email, recipient_email, msg.as_string())

        flash("Emails sent successfully!", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("An error occurred while sending the emails.", "error")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
