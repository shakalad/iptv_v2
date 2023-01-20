import email
import imaplib
import re


def get_transaction_verification_code():
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login("shakalad92@gmail.com", "lxjtbhcqklmtvbgv")
    mail.select('inbox')
    _, msgnums = mail.search(None, '(FROM "support@vipdrive.net")')
    transaction_verification_code = []

    for msgnum in msgnums[0].split():
        _, data = mail.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = part.get_payload(decode=True).decode()
                transaction_verification_code.append(body)

    code = re.search("<li>код подтверждения - <b>(.*?)</b></li>", transaction_verification_code[-1])

    return code.group(0).split("<b>")[-1].split("</b>")[0]