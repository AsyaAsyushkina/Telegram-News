from xml.etree.ElementTree import tostring

# import feedparser
# rss_url = "https://kill-the-newsletter.com/feeds/tv52d3mc8fcm1af5z864.xml"

import email
import imaplib
import json

with open("config.json", "r") as f:
    config = json.load(f)

connection_to_server = imaplib.IMAP4_SSL("imap.gmail.com")
connection_to_server.login("learnainews2026@gmail.com", "")


# mail_feed = feedparser.parse(rss_url)
# print(mail_feed)
#
# # returns the link of the blog
# # and number of entries(blogs) in the site.
# print("is feed link" + mail_feed.feed.link)
# print("len is " + str(len(mail_feed.entries)))
# # print("detail is " + mail_feed.feed.subtitle_detail)
#
#
# # Details of individual blog can
# # be accessed by using attribute name
# print(mail_feed.entries[0].title)
# print(mail_feed.entries[0].link)
# print(mail_feed.entries[0].author)
# print(mail_feed.entries[0].published)
# print(mail_feed.entries[0].guid)
# print(mail_feed.entries[0].description)
# print(mail_feed.entries[1].guid)

# # Getting lists of tags and authors.
# tags = [tag.term for tag in mail_feed.entries[0].tags]
# authors= [author.name for author in mail_feed.entries[0].authors]