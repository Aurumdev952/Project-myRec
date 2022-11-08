import click

# commmand groups
@click.group
def master():
    pass


@click.group
def getRec():
    pass


@click.group
def functions():
    pass

# optlist
CATEGORIES = {
    "t": "test",
    "c": "CAT",
    "e": "exam"
}

# optlist 
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
    print(title, subject, value, max_value, CATEGORIES[category])



@click.command()
@click.argument("id", type=int, required=True)
@click.option("-f", "field", prompt="Enter the field of the record you want to update", type=str, required=True)
@click.argument("new_value", type=int, required=True)
def updateRec(id, field, new_value):
    """
    Update a record.
    """
    print(id, field, new_value)


@click.command()
@click.argument("id", type=int, required=True)
def deleteRec(id):
    '''
    delete record
    '''
    print(id)


@click.command()
@click.argument("id", type=int, required=True)
def ById(id):
    '''
    retrieve record by id
    '''
    print(id)


@click.command()
@click.argument("subject", type=str, required=True)
def BySubject(subject):
    '''
    retrieve record by subject
    '''
    print(subject)


@click.command()
@click.argument("category", type=click.Choice(CATEGORIES.keys()), required=True)
def ByCategory(category):
    '''
    retrieve record by category
    '''
    print(category)




# register all commands
master.add_command(createRec)
master.add_command(updateRec)
master.add_command(deleteRec)
master.add_command(getRec)

getRec.add_command(ById)
getRec.add_command(ByCategory)
getRec.add_command(BySubject)


if __name__ == "__main__":
    master()

