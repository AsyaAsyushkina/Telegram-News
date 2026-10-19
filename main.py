from mail import get_first_mail_info
from AI import ai_reprocessing
from bot import send_message

mail_info = get_first_mail_info()
while mail_info is not None:
    response = ai_reprocessing(mail_info)
    send_message(response)
    mail_info = get_first_mail_info()