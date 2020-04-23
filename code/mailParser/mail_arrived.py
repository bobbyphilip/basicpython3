#!/usr/bin/python3
import sys
import email
import log
import base64
import datetime
from email import policy

logger = log.setup_logger("Mail")
def get_text_from_email():
    sys.stdin = sys.stdin.detach()
    msg = email.message_from_binary_file(sys.stdin, policy=policy.default) 
    email_sender = msg['from']
    logger.info('The email is from '+email_sender)
    if msg.is_multipart():
        logger.debug('This is a multipart email')
        for part in msg.walk():
            logger.debug(part.get_content_type())
            if part.get_content_type() == "text/plain":
                if part.is_attachment():
                    logger.debug('Skipping attachment')
                else:
                    email_bytes = part.get_payload(decode=True)
                    break
    else:
        logger.debug('This is not a multipart email')
        email_bytes = msg.get_payload(decode=True)
    email_text = email_bytes.decode(encoding='UTF-8')
    logger.info('The text of the email '+email_text)
    return email_text

def main():
    try:
        if len(sys.argv) >1:
            email_body = sys.argv[1]
        else:
            logger.info('Got a new email')
            email_body = get_text_from_email()
        email_array = email_body.splitlines()
        full_dict = utils.read_dict_from_file()
        for email_text in email_array:
            logger.debug("In the loop %s",email_text)

    except Exception as e:
        logger.exception('Exception!!')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
