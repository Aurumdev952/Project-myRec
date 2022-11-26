# import click
import rich_click as click 
import api.api_router as api
import config.config as config
import display as d





# hide_input=True

click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.STYLE_ERRORS_SUGGESTION = "magenta italic"
click.rich_click.ERRORS_SUGGESTION = "Try running the '--help' flag for more information."
click.rich_click.ERRORS_EPILOGUE = "To find out more, visit [link=https://mytool.com]https://mytool.com[/link]"
click.rich_click.STYLE_OPTION = "bold cyan"
# commmand groups


@click.group
def master():
    pass

@click.group
def user():
    """
    👈 user commands 
    
    """
    pass

@click.group
def getRec():
    """
    retrieve rec
    """
    pass

# @click.group
# def functions():
#     pass

# @click.group
# def createAccount():
#     print("hello world")

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
    if config.check_save() == True:
        data = {}
        user = config.get_save()
        userid = user.getId()
        data["user"] = userid
        data["title"] = title
        data["subject"] = subject
        data["value"] = value
        data["max_value"] = max_value
        data["category"] = CATEGORIES[category]

        res = api.create_rec(data)
        if res != False:
            d.print_rec(res, "Rec created")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")




 

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
    if config.check_save() == True:
        data = {}
        data[field] = new_value
        res = api.update_rec(id, data)
        if res != False:
            d.print_rec(res, "Updated")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")






@click.command()
def hello():
    print("hello")

@click.command()
@click.argument("id", type=str, required=True)
def deleteRec(id):
    '''
    delete record
    '''
    if config.check_save() == True:
        res = api.delete_rec(id)
        if res != False:
            d.print_rec(res, "Deleted")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")



    


@click.command()
@click.argument("id", type=str, required=True)
def ById(id):
    '''
    retrieve record by id
    '''
    if config.check_save() == True:
        user = config.get_save()
        userid = user.getId()
        res = api.get_byid(userid, id)
        if res != False:
            d.print_rec(res, "access complete")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")





@click.command()
@click.argument("subject", type=str, required=True)
def BySubject(subject):
    '''
    retrieve record by subject
    '''
    if config.check_save() == True:
        user = config.get_save()
        userid = user.getId()
        res = api.get_bysubject(userid, subject)
        if res != False:
            d.print_table_all(res["records"], "access complete")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")



@click.command()
@click.argument("category", type=click.Choice(CATEGORIES.keys()), required=True)
def ByCategory(category):
    '''
    retrieve record by category
    '''
    if config.check_save() == True:
        user = config.get_save()
        userid = user.getId()
        res = api.get_bycategory(userid, CATEGORIES[category])
        if res != False:
            d.print_table_all(res["records"], "access complete")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")



@click.command()
def All():
    '''
    get all user records
    '''
    if config.check_save() == True:
        user = config.get_save()
        userid = user.getId()
        res = api.get_all(userid)
        if res != False:
            d.print_table_all(res["records"], "all rec")
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")




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
    
    if res != False:
        config.initialiseSave(res["_id"], res["username"], res["email"], password, res["createdAt"])
        d.output("Successfully saved", mode="success")
        d.print_user(res)
    else:
        d.output("Error has occurred, please try again", mode="error")

    # print(name, email, password)

@click.command()
# @click.argument("id", type=int, required=True)
@click.option("-f", "field", prompt="Enter the field of the user profile you want to update", type=click.Choice(USER), required=True)
@click.option("-nv", "new_value", prompt="Enter the new value", type=str, required=True)
def updateUser(field, new_value):
    """
    Update a user
    """
    if config.check_save() == True:
        user = config.get_save()
        userid = user.getId()
        data = {}
        data[field] = new_value
        # d.print(data)
        res = api.update_user(userid, data)
        
        
        if res != False:
            config.update_save(field, new_value)
            d.print_user(res)
            
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")








@click.command()
@click.option('-e', 'email', prompt="Enter email", type=str, required=True)
@click.option('-p', 'password', prompt="Enter password", type=str, required=True, hide_input=True)
def loginUser(email, password):
    '''Logs in a user'''
    data = {}
    data["email"] = email
    data["password"] = password
    res = api.validate_user(data)
    
    if res != False:
        try:
            print(config.initialiseSave(res["_id"], res["username"], res["email"], password, res["createdAt"]))
            d.output("you are now logged in", mode="success")
            # print("you are now logged in")
            d.print_user(res)
            
        except:
            d.output("login failed", mode="error")
            # print('login failed')    
        # print(res)
    else:
        d.output("Error has occurred, please try again", mode="error")
   
    

@click.command()
def checkUserprofile():
    '''check your user profile'''
    if config.check_save() == True:
        user = config.get_save()
        userid = user.getId()
        res = api.get_user(userid)
        if res != False:
            # d.print_json(res)
            d.print_user(res)
        else:
            d.output("Error has occurred, please try again", mode="error")
    else:
        d.output("Error, please create an account or login", mode="error")

   
    








# register all commands
master.add_command(createRec)
master.add_command(updateRec)
master.add_command(deleteRec)
master.add_command(getRec)
master.add_command(user)

user.add_command(createUser)
user.add_command(loginUser)
user.add_command(updateUser)
user.add_command(checkUserprofile)

getRec.add_command(All)
getRec.add_command(ById)
getRec.add_command(ByCategory)
getRec.add_command(BySubject)

# createAccount.add_command(createUser)
# createAccount.add_command(loginUser)



if __name__ == "__main__":
    master()


