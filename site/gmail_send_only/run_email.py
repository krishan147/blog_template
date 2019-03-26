from __future__ import print_function

def send_email(message_details,email_address):

    import httplib2
    import os
    from apiclient import discovery
    from oauth2client import client
    from oauth2client import tools
    from oauth2client.file import Storage
    from gmail_send_only import auth

    SCOPES = 'https://mail.google.com/'
    CLIENT_SECRET_FILE = 'gmail_send_only/client_secret.json'
    APPLICATION_NAME = 'Gmail API Python Quickstart'
    authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
    credentials = authInst.get_credentials()

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    from gmail_send_only import send_email

    form_id = message_details[0]
    form_name = message_details[1]
    form_email = message_details[2]
    form_message = message_details[3]

    message_layout = {
        'form_id':form_id,
        'form_name':form_name,
        'form_email':form_email,
        'form_message':form_message
    }

    sendInst = send_email.send_email(service)
    message = sendInst.create_message_with_attachment(email_address,email_address,'From Blog Template',str(message_layout), 'gmail_send_only/image.jpg' )
    sendInst.send_message('me',message)

    return message