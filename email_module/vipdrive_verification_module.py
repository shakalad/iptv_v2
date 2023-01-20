import email
import imaplib
import re


def get_vipdrive_registration_verification_code():
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login("shvilcenkokn@gmail.com", "tfcrutfucvgorkcg")
    mail.select('inbox')
    _, msgnums = mail.search(None, '(FROM "support@vipdrive.net")')
    verification_code = []

    for msgnum in msgnums[0].split():
        _, data = mail.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = str(part.get_payload())
                code = re.search("<b>(.*?)</b>", body).group(0).split("<b>")[-1].split("</b>")[0]
                verification_code.append(code)

    return verification_code[-1]
