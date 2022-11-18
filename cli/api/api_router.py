import asyncio
import httpx

# get

async def get(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.json()



# put request
async def put(url, update):
    async with httpx.AsyncClient() as client:
        r = await client.put(url, json=update)
        return r.json()


# post request
async def post(url, data):
    timeout = httpx.Timeout(connect=None, read=None, write=None, pool=None)
    async with httpx.AsyncClient(timeout=timeout) as client:
        r = await client.post(url, json=data)
        if r.status_code == 200:
            print(r.json())
            return r.json()


# delete request
async def delete(url):
    async with httpx.AsyncClient() as client:
        r = await client.delete(url)
        return r.json()


def get_data(url):
    return asyncio.run(get(url))


def post_data(url, data):
    return asyncio.run(post(url, data))

def update_data(url, updates):
    return asyncio.run(put(url, updates))

def delete_data(url):
    return asyncio.run(delete(url))

# import api_client as c

main_url = "https://myrec.onrender.com/api/"


def create_rec(data):
    url = main_url + "create/record"
    return post_data(url, data)

def create_user(data):
    url = main_url + "create/user"
    return post_data(url, data)


def update_rec(id, data):
    url = main_url + "update/rec/" + id 
    return update_data(url, data)

def update_user(id, data):
    url = main_url + "update/rec" + id
    return update_data(url, data)

def delete_rec(id):
    url = main_url + "delete/rec/" + id
    return delete_data(url)

def get_byid(userid, id):
    url = main_url + "get/byid/" + userid + "/" + id
    return get_data(url)

def get_bycategory(userid, category):
    url = main_url + "get/bycategory/" + userid + "/" + category
    return get_data(url)

def get_bysubject(userid, subject):
    url = main_url + "get/bysubject/" + userid + "/" + subject
    return get_data(url)

def get_all(userid):
    url = main_url + "get/all/" + userid 
    return get_data(url)


def get_user(userid):
    url = main_url + "get/" + userid 
    return get_data(url)





















