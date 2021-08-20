from fastapi import APIRouter
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from app.db import database, db_users

router = APIRouter()

@router.get("/")
async def read_spreadsheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('app/vaksinasicepu200821-ef38953eb28c.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Form Vaksin').sheet1
    data = sheet.get_all_records()
    print(data)
    return data