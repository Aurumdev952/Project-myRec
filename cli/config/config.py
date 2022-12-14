import pickle
from rich.console import Console
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
    try:
        with open(filename, 'rb') as dbfile:
            dbfile = open(filename, 'rb')     
            db = pickle.load(dbfile)
            return db['data']
    except:
        return None
        

        


def check_save():
    c = Console()
    with c.status("[bold green]loading save...[/]", spinner="dots7") as status:
        data = loadData()
        if data != None:
            c.print("Save found", style="bold green")
            return True
        else:
            c.print("Save not found", style="bold red")
            # print("False...............................")
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









    