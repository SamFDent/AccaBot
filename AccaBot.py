import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getResponseData():
    # Set scopes necessary to access the Google Sheet
    scope = ["https://www.googleapis.com/auth/spreadsheets"
            ,"https://www.googleapis.com/auth/drive"
            ,"https://www.googleapis.com/auth/drive.file"
            ,"https://www.googleapis.com/auth/drive.readonly"
            ,"https://www.googleapis.com/auth/spreadsheets.readonly"]

    # Set authorisation credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Retrieve the AccaBot forms responses
    gsheet = client.open('AccaBot')
    responses = gsheet.worksheet('Form Responses 2')
    predictions = responses.get_all_records()

    return predictions
