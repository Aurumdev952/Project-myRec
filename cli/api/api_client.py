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
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=data)
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






