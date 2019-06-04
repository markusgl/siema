from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.google.com/auth/documents']

# The ID of a sample document.
#DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'
DOCUMENT_ID = '1HbBlEtUOTAJtYu2ZYl7qGqZrUjjTcG_0Wp0W8ZSpqvw'

def login():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(ROOT_DIR + 'token.pickle'):
        with open(ROOT_DIR + 'token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                ROOT_DIR + 'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(ROOT_DIR + 'token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    #print('The title of the document is: {}'.format(document.get('title')))
    endIndex = document.get('body')['content'][-1]['endIndex']

    return service, endIndex-1


def insert_text(text):
    service, endIndex = login()

    requests = [
         {
            'insertText': {
                'location': {
                    'index': endIndex,
                },
                'text': '\n' + text
            }
        }
    ]

    result = service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': requests}).execute()

    print(result)


#if __name__ == '__main__':
    #login()
#    insert_text('Messung1')
