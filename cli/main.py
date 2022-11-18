import click
import api.api_router as api
import config.config as config


# hide_input=True

# commmand groups


@click.group
def master():
    pass

@click.group
def user():
    pass

@click.group
def getRec():
    pass

@click.group
def functions():
    pass

@click.group
def createAccount():
    print("hello world")

# optlist
CATEGORIES = {
    "t": "test",
    "c": "CAT",
    "e": "exam"
}

USER = [
    "username",
    "password"
]
REC = [
    "title",
    "subject",
    "value",
    "max_value",
    "category"
]

#  
@click.command()
@click.option("-t", "title", prompt="Enter the title of the record", type=str, required=True) 
@click.option("-s", "subject", prompt="Enter the subject of the record", type=str, required=True)
@click.option("-v", "value", prompt="Enter the value of the record", type=int, required=True)
@click.option("-mv", "max_value", prompt="Enter the maximum value of the record", type=int, required=True)
@click.option("-c", "category", prompt="Enter the category of the record", type=click.Choice(CATEGORIES.keys()), default="t", required=True)
def createRec(title, subject, value, max_value, category):
    """
    Create a new record.
    """
    if config.check_save == True:
        data = {}
        user = config.get_save()
        userid = user.getId()
        data["user"] = userid
        data["title"] = title
        data["subject"] = subject
        data["value"] = value
        data["max_value"] = max_value
        data["category"] = CATEGORIES[category]

        print(api.create_rec(data))
    else:
        print("Error, please create an account or login")




 

    # print(title, subject, value, max_value, CATEGORIES[category])



@click.command()
@click.argument("id", type=str, required=True)
@click.option("-f", "field", prompt="Enter the field of the record you want to update", type=click.Choice(REC), required=True)
@click.option("-nv", "new_value", prompt="Enter the new value", type=str, required=True)
# @click.argument("new_value", type=str, required=True)
def updateRec(id, field, new_value):
         
    """
    Update a record.
    """
    if config.check_save == True:
        data = {}
        data[field] = new_value
        print(api.update_rec(id, data))
    else:
        print("Error, please create an account or login")






@click.command()
def hello():
    print("hello")

@click.command()
@click.argument("id", type=str, required=True)
def deleteRec(id):
    '''
    delete record
    '''
    if config.check_save == True:
        print(api.delete_rec(id))
    else:
        print("Error, please create an account or login")



    


@click.command()
@click.argument("id", type=str, required=True)
def ById(id):
    '''
    retrieve record by id
    '''
    if config.check_save == True:
        user = config.get_save()
        userid = user.getId()
        print(api.get_byid(userid, id))
    else:
        print("Error, please create an account or login")





@click.command()
@click.argument("subject", type=str, required=True)
def BySubject(subject):
    '''
    retrieve record by subject
    '''
    if config.check_save == True:
        user = config.get_save()
        userid = user.getId()
        print(api.get_bysubject(userid, subject))
    else:
        print("Error, please create an account or login")



@click.command()
@click.argument("category", type=click.Choice(CATEGORIES.keys()), required=True)
def ByCategory(category):
    '''
    retrieve record by category
    '''
    if config.check_save == True:
        user = config.get_save()
        userid = user.getId()
        print(api.get_bycategory(userid, CATEGORIES[category]))
    else:
        print("Error, please create an account or login")



@click.command()
def All():
    '''
    get all user records
    '''
    if config.check_save == True:
        user = config.get_save()
        userid = user.getId()
        print(api.get_all(userid))
    else:
        print("Error, please create an account or login")




# user functions

@click.command()
@click.option('-n', 'name', prompt="Enter username", type=str, required=True)
@click.option('-e', 'email', prompt="Enter email", type=str, required=True)
@click.option('-p', 'password', prompt="Enter password", type=str, required=True, hide_input=True)
def createUser(name, email, password):
    '''Create a new user'''

    data = {}
    data["username"] = name
    data["email"] = email
    data["password"] = password

    res = api.create_user(data)
    print(config.initialiseSave(res["_id"], res["username"], res["email"], password, res["createdAt"]))

    # print(name, email, password)

@click.command()
@click.argument("id", type=int, required=True)
@click.option("-f", "field", prompt="Enter the field of the user profile you want to update", type=click.Choice(USER), required=True)
@click.argument("new_value", type=int, required=True)
def updateUser(id, field, new_value):
    """
    Update a user
    """
    if config.check_save == True:
        user = config.get_save()
        userid = user.getId()
        data = {}
        data[field] = new_value
        print(api.update_user(userid, data))
        config.update_save(field, new_value)
    else:
        print("Error, please create an account or login")








@click.command()
@click.option('-e', 'email', prompt="Enter email", type=str, required=True)
@click.option('-p', 'password', prompt="Enter password", type=str, required=True, hide_input=True)
def loginUser(email, password):
    '''Create a new user'''
    # data = {}
    # data["email"] = email
    # data["password"] = password
    # res = api.get_user(data)
    # print(config.initialiseSave(res["_id"], res["username"], res["email"], password, res["createdAt"]))
    pass
    

@click.command()
def checkUserprofile():
    '''check your user profile'''
    pass
    








# register all commands
master.add_command(createRec)
master.add_command(updateRec)
master.add_command(deleteRec)
master.add_command(getRec)
master.add_command(user)

user.add_command(createUser)
user.add_command(loginUser)
user.add_command(updateUser)

getRec.add_command(All)
getRec.add_command(ById)
getRec.add_command(ByCategory)
getRec.add_command(BySubject)

createAccount.add_command(createUser)
createAccount.add_command(loginUser)



if __name__ == "__main__":
    master()


