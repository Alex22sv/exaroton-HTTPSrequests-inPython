import aiohttp
import asyncio
import json

api_token = "Insert your API token here"
serverID = "Insert your server ID here"
base_url = "https://api.exaroton.com/v1"
ownCredits = {"useOwnCredits" : True}



async def main():
    resp = await api_request(f"/server/{serverID}/start/", "POST", ownCredits)
    print(json.dumps(resp))


async def api_request(path, method, data):
    headers = {'Authorization': 'Bearer ' + api_token}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=base_url + path, data=data) as response:
            return await response.json()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''
Start an exaroton server that you have shared access to with your own credits.

Example response:
{
  "success": true,
  "error": null,
  "data": null
}
'''
