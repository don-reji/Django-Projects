# import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# this is for establishing to Google Calendar
def get_calendar_service():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(script_dir, "credentials.json")

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path , SCOPES
            )
            creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)

# add / update tasks to google calendar
def sync_with_google_calendar(task):
    service = get_calendar_service()

    event = {
        "summary": task.title,
        "description": task.description,
        
        # isoformat() converts our dateTime object (start_date and due_date since they are dateTime in models) 
        # into strings in ISO 8601 format needed for google calendar
        "start": {"dateTime": task.start_date.isoformat() , "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": task.due_date.isoformat() , "timeZone": "Asia/Kolkata"},
    }

    calendar_id = "primary"  

    try:
        # If task has an ID, update the event; otherwise, create a new event
        if task.google_calendar_id:
            service.events().update(
                calendarId=calendar_id,
                eventId=task.google_calendar_id,
                body=event,
            ).execute()
        else:
            result = service.events().insert(
                calendarId=calendar_id,
                body=event,
            ).execute()

            # when tasks object created google_calendar_id is empty, then when event is created 
            # google calendar assigns that value

            # Save the eventID in your google_calendar_id field 
            task.google_calendar_id = result["id"]
            task.save()

        print("Task synced with Google Calendar successfully!")

    except HttpError as error:
        print(f"An error occurred while syncing with Google Calendar: {error.content}")

def delete_event(event_id):
    service=get_calendar_service()
    calendarId="primary"
    try:
        service.events().delete(calendarId=calendarId, eventId=event_id).execute()
        print("Event deleted successfully from Google Calendar.")
    except HttpError as error:
        print(f"An error occurred while deleting the event: {error}")

if __name__ == "__main__":
    try:
        service = get_calendar_service()
        print('Connection to Google Calendar API established')
    except HttpError as error:
        print(f"An error occurred: {error}")