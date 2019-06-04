from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import  Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1hcCa3ZhUSS83fZlQuLX2X68NlB_te9kV5QPUJxuA5fI'
RANGE_NAME = 'Tabellenblatt1!B2:C2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
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

    service = build('sheets', 'v4', credentials=creds)

    return service


def get_spec_size():
    service = main()
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    spec_value = None
    if not values:
        print('No data found.')
    else:
        spec_value = values[0][0]

    return spec_value


def write_actual_size(value):
    service = main()

    values = [
        [
            value
        ],
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    value_input_option = 'USER_ENTERED'
    range_name = "Tabellenblatt1!C2:C2"
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))


if __name__ == '__main__':
    #main()
    write_actual_size('12.03')
    #spec_value = get_spec_size()
    #print(spec_value)
