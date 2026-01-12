
# # src/utils/alerts.py
# import os
# import smtplib
# from email.mime.text import MIMEText
# import requests

# def send_email(subject: str, body: str) -> bool:
#     host = os.getenv("SMTP_HOST")
#     port = int(os.getenv("SMTP_PORT", "587"))
#     user = os.getenv("SMTP_USER")
#     pwd = os.getenv("SMTP_PASSWORD")
#     to = os.getenv("ALERTS_EMAIL_TO")
#     if not all([host, port, user, pwd, to]):
#         return False  # Missing config → skip
#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = user
#     msg["To"] = to
#     with smtplib.SMTP(host, port) as server:
#         server.starttls()
#         server.login(user, pwd)
#         server.send_message(msg)
#     return True

# def send_slack(text: str) -> bool:
#     webhook = os.getenv("SLACK_WEBHOOK_URL")
#     if not webhook:
#         return False  # Missing config → skip
#     try:
#         requests.post(webhook, json={"text": text}, timeout=10)
#         return True
#     except Exception:
#         return False
