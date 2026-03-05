import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your report data
report = {
    "plate": "KDA123B",
    "lane_position": "RIGHT",
    "violation": "Overlapping",
    "timestamp": "2025-06-24T13:42:10",
    "location": "Academic Highway A104"
}

# Email config
sender_email = "mishimihammed@gmail.com"
receiver_email = "mishimohajuma@gmail.com"
app_password = "sbda duyl ghko giqz"  # NOT your normal Gmail password

# Build the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Traffic Violation Report"

# Convert dict to pretty JSON string
json_body = json.dumps(report, indent=4)
msg.attach(MIMEText(json_body, 'plain'))

# Send email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
        print("✅ Email sent successfully.")
except Exception as e:
    print("❌ Failed to send email:", e)
