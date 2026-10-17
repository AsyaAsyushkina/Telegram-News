from xml.etree.ElementTree import tostring

# import feedparser
# rss_url = "https://kill-the-newsletter.com/feeds/tv52d3mc8fcm1af5z864.xml"

import email
import imaplib
import json

with open("config.json", "r") as f:
    config = json.load(f)

connection_to_server = imaplib.IMAP4_SSL("imap.gmail.com")
connection_to_server.login(config["email"], config[ "password"])
connection_to_server.select("inbox")

status, data = connection_to_server.search(None, 'UNSEEN', 'FROM "thebatch@deeplearning.ai"')
id_mails = data[0].split()
print(status, " ", id_mails)
