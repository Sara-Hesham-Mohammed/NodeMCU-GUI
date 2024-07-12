import firebase_admin as fAdmin
from firebase_admin import credentials, db


class Firebase:

    def __init__(self):
        # Initialize the app with a service account, granting admin privileges
        cred = credentials.Certificate("../key/rt-screen-afa55-firebase-adminsdk-luskh-d798b4267d.json")
        fAdmin.initialize_app(cred, {
            'databaseURL': 'https://rt-screen-afa55-default-rtdb.firebaseio.com/'
        })

        self.database = db.reference('sensorData')

    # Example usage
    def get_data(self,field):
        data = self.database.child(field).get()
        return data

    x=100

    while x>0:
        # Example usage
        distance_travelled = get_data('distanceTravelled')
        value = get_data('value')

        print('Distance Travelled:', distance_travelled)
        print("Value:", value)

        x-=1

