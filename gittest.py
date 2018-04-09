"""docstring."""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
# use creds to create a client to interact with the Google Drive API
##scope = ['https://spreadsheets.google.com/feeds']
scope = [
 #   'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'servicecred.json', scope)
gc = gspread.authorize(creds)
##
##gc = client.open("Legis").sheet1

wb = gc.open('Legis')
##worksheet = sh.worksheet("legislators-current")
worksheet = wb.worksheet("legislators-current")
##worksheet = sh.worksheet("legislators-current")

list_of_hashes = worksheet.get_all_records()
pprint.pprint(list_of_hashes[4])
values_list = worksheet.row_values(1)
print(values_list)
##SCOPES = 

