import os


## Test bucket
async def testConnect(client):
    async with client as s3:
        Key = "my_key"
        await s3.put_object(Bucket = os.environ.get("BUCKET"), Key = Key, Body = str({"test" : "test text", "message" : "bla bla"}).encode())
        resp = await s3.get_object(Bucket = os.environ.get("BUCKET"), Key = Key)
        body = await resp["Body"].read()
        print(body)
        await s3.delete_object(Bucket = os.environ.get("BUCKET"), Key = Key)
        print("Ok for BUCKET")
        return body

 
## Send video 
async def putVideo(client, key, video):
    async with client as s3:
        await s3.put_object(Bucket = os.environ.get("BUCKET"), Key = key, Body = video)
        print("Put video is ok")


## Send json
async def putJson(client, key, json):
    async with client as s3:
        await s3.put_object(Bucket = os.environ.get("BUCKET"), Key = key, Body = str(json).encode())
        print("Put JSON is ok")