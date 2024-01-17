# tryon/config.py
RAPID_API_KEY = "6069c0f8fcmsh466fdb49c83196bp1e658djsn70d20a244376"
LOOK_URI = None
AVATAR_URI = None

def update_config(look_uri, avatar_uri):
    global LOOK_URI, AVATAR_URI
    LOOK_URI = look_uri
    AVATAR_URI = avatar_uri
