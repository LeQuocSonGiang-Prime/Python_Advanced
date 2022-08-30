import pyrebase

# Your credentials after create a app web project.
config = {
  'apiKey': "AIzaSyAMV3KZ02RrzJLSVgVoeAihHdUg7oc82LA",
  'authDomain': "python-connect-database.firebaseapp.com",
  'databaseURL': "https://python-connect-database-default-rtdb.firebaseio.com",
  'projectId': "python-connect-database",
  'storageBucket': "python-connect-database.appspot.com",
  'messagingSenderId': "577599395407",
  'appId': "1:577599395407:web:0f716862f15dde7136fc3a",
  'measurementId': "G-0WVCPQ0SVS"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def uploadFile(path_on_cloud, path_local):
    storage.child(path_on_cloud).put(path_local)