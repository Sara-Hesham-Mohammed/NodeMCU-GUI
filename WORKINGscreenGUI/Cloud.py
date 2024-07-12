import firebase_admin
from firebase_admin import credentials

# Initialize the app with a service account, granting admin privileges
cred = credentials.Certificate("key/racing-team-screen-52268-firebase-adminsdk-ahivf-e1ea9a7cf8.json")
firebase_admin.initialize_app(cred)
