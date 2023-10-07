import email
import imaplib
import re


def get_ottplayer_registration_activation_link():
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login("ipservice2023@gmail.com", "duswmhrthxszwhcl")
    mail.select('inbox')
    _, msgnums = mail.search(None, '(FROM "support@ottplayer.tv")')
    activation_links = []

    for msgnum in msgnums[0].split():
        _, data = mail.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = part.get_payload(decode=True).decode()
                activation_link = re.findall(r'href=[\'"]?([^\'" >]+)', body)[4]
                activation_links.append(activation_link)

    return activation_links[-1]
