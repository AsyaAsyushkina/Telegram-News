import imaplib
import email
from email import policy
from config import EMAIL, PASSWORD, SENDERS


if not EMAIL or not PASSWORD or not SENDERS:
    raise NameError('EMAIL, PASSWORD, SENDERS must be set')

connection_to_server = imaplib.IMAP4_SSL("imap.gmail.com")
connection_to_server.login(EMAIL, PASSWORD)
connection_to_server.select("inbox")
id_mails = []

def build_sender_search(sender_list):
    if not sender_list:
        return 'ALL'

    query = f'FROM "{sender_list[0]}"'
    for sender in sender_list[1:]:
        query = f'OR {query} FROM "{sender}"'
    return f'({query})'

def get_id_mails():
    print("=" * 40)
    print(f"DEBUG SENDERS LIST: {SENDERS}")
    print(f"DEBUG SENDERS TYPE: {type(SENDERS)}")
    print("=" * 40)
    if True:
        raise NameError(f"DEBUG SENDERS LIST: {SENDERS}")
    status, data = connection_to_server.search(None, 'UNSEEN', build_sender_search(SENDERS))
    new_id_mails = data[0].split()
    id_mails.extend(new_id_mails)

def get_first_mail_id():
    get_id_mails()
    first_mail = None
    if len(id_mails) != 0:
        first_mail = id_mails[0]
        id_mails.remove(first_mail)
    return first_mail

def get_first_mail_info():
    mail_i = get_first_mail_id()
    if mail_i is None:
        return None
    status_i, data_i = connection_to_server.fetch(mail_i, "(RFC822)")
    mail_info = email.message_from_bytes(data_i[0][1], policy=policy.default)
    body = mail_info.get_body(preferencelist=('plain', 'html'))
    sender = mail_info["From"]
    subject = mail_info["Subject"]
    date = mail_info["Date"]
    mail_to_text = "Sender: " + sender + "\nSubject: " + subject + "\nDate: " + date + "\nNews" + body.get_content()
    return mail_to_text
