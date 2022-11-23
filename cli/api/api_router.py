import asyncio
import httpx
# import requests
# from requests.adapters import HTTPAdapter, Retry

# # get

# def req_post(data):
#     try: 
#         r = requests.post("https://myrec.onrender.com/api/validate/user", json=data)
#         print(r.json())
#         return r.json(), r.status_code
#     except Exception as e:
#         return {
#             "status": 500,
#             "message": str(e)
#         }, 500
        

# def req_post2(data):
#     try:
#         url = 'https://myrec.onrender.com/api/validate/user'
#         response = requests.post(url, json=data)

#         session = requests.Session()
#         retry = Retry(connect=3, backoff_factor=0.5)
#         adapter = HTTPAdapter(max_retries=retry)
#         session.mount('http://', adapter)
#         session.mount('https://', adapter)

#         url = 'https://reqres.in/api/users'
#         response = session.get(url)
#         return response.json(), response.status_code

  
#     except Exception as e:
#         return {
#             "status": 500,
#             "message": str(e)
#         }, 500
        

async def get(url):
    timeout = httpx.Timeout(connect=None, read=None, write=None, pool=None)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(url)
            return resp.json(), resp.status_code
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }, 500
        
        # resp = await client.get(url)
        # return resp.json()
        





# put request
async def put(url, update):
    timeout = httpx.Timeout(connect=None, read=None, write=None, pool=None)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            r = await client.put(url, json=update)
            return r.json(), r.status_code
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }, 500
        


# post request
async def post(url, data):
    timeout = httpx.Timeout(connect=None, read=None, write=None, pool=None)
    async with httpx.AsyncClient(timeout=timeout) as client:
        
        try:
            r = await client.post(url, json=data)
            print(r.json())
            return r.json(), r.status_code
        except Exception as e:
            return {
                "status": 500,
                "message": str(e)
            }, 500
        


# delete request
async def delete(url):
    timeout = httpx.Timeout(connect=None, read=None, write=None, pool=None)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            r = await client.delete(url)
            return r.json(), r.status_code
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }, 500
        


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
    req, status_code = post_data(url, data)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def create_user(data):
    url = main_url + "create/user"
    req, status_code = post_data(url, data)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False


def update_rec(id, data):
    url = main_url + "update/rec/" + id 
    req, status_code = update_data(url, data)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def update_user(id, data):
    url = main_url + "update/rec" + id
    req, status_code = update_data(url, data)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def delete_rec(id):
    url = main_url + "delete/rec/" + id
    req, status_code = delete_data(url)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def get_byid(userid, id):
    url = main_url + "get/byid/" + userid + "/" + id
    req, status_code = get_data(url)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def get_bycategory(userid, category):
    url = main_url + "get/bycategory/" + userid + "/" + category
    req, status_code = get_data(url)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def get_bysubject(userid, subject):
    url = main_url + "get/bysubject/" + userid + "/" + subject
    req, status_code = get_data(url)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False

def get_all(userid):
    url = main_url + "get/all/" + userid 
    req, status_code = get_data(url)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False
 
    


def get_user(userid):
    url = main_url + "get/" + userid 
    req, status_code = get_data(url)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False
    
def validate_user(data):
    url = main_url + "validate/user"
    req, status_code = post_data(url, data)
    print(req)
    if status_code == 200:
        return req
    else:
        print(status_code)
        return False
    






















