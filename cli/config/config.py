import pickle
import os

absolute_path = os.path.dirname(__file__)
relative_path = "configdb.data"
FILE = os.path.join(absolute_path, relative_path)
# FILE = "configdb.data"
def storeData(data, filename=FILE):  
    dt = {}
    dt["data"] = data
    # Its important to use binary mode
    # with open(filename, "wb") as f:
    #     pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    with open(filename, 'rb') as dbfile:
        dbfile = open(filename, 'wb')
        pickle.dump(dt, dbfile)                     

  
def loadData(filename=FILE):
    # for reading also binary mode is important
    with open(filename, 'rb') as dbfile:
        dbfile = open(filename, 'rb')     
        db = pickle.load(dbfile)
        return db['data']


def check_save():
    data = loadData()
    if data != None:
        print("True....................")
        return True
    else:
        print("False...............................")
        return False

class Save():
    def __init__(self, id, username, email, password, date):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.date = date

    def update(self, field, data):
        if field == 'username':
            self.username = data
        elif field == 'password':
            self.password = data
        elif field == 'email':
            self.email = data

    def getId(self):
        return self.id
    def getPassword(self):
        return self.password


def initialiseSave(id, username, email, password, date):
    saveObj = Save(id, username, email, password, date)
    storeData(saveObj)
    return saveObj

def get_save():
    return loadData()


def update_save(field, data):
    save = loadData()
    save.update(field, data)
    storeData(save)






    