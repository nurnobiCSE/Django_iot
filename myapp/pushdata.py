import pyrebase
config = {
    "apiKey": "AIzaSyBIwNqdqEekxvWJMSDqbxTyc5tFpZjW0OA",
    "authDomain": "webiot-6ac14.firebaseapp.com",
    "databaseURL": "https://webiot-6ac14-default-rtdb.firebaseio.com",
    "projectId": "webiot-6ac14",
    "storageBucket": "webiot-6ac14.appspot.com",
    "messagingSenderId": "278225565212",
    "appId": "1:278225565212:web:7b428d3e171afaa7f851d9",
     
}

firebase= pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
# data = {
#     "box1":1,
#     "box2":0,
#     "time1":0,
#     "time2":0
# }
# database.child("Data").child("reminder").set(data)
 

