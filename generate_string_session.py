from pyrogram import Client

API_KEY = int(input("Enter API KEY:2451378"))
API_HASH = input("Enter API HASH:90e08dbcdc8df276b83f57f80152eb9a")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
