from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

from IOstream import rain


SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] 
SERVICE_ACCOUNT_FILE = 'keys.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1C8807pXtxPTH3lFHhoDYQYF4ctDbArvKy2n1ZolwzMU'




    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Sheet1!A1:B2").execute()
values = result.get('values', [])

#traffic = run_traffic()
#visbility = run_weather()

update1 = "Visbility,0,Traffic,1"
update2 = "Visibility,0,Traffic,1"

data = [["",update1]]


request = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Sheet1!A1:B1", valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS", body={"values":data}).execute()
print(request)
