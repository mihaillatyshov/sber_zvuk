import os
from flask import Flask, abort, jsonify, make_response, request
import urllib.request
import shutil
import asyncio
import aioboto3
from dotenv import load_dotenv
import bucket

## Loding super puper secret data!!!
envconfig = load_dotenv()

## Create server app
app = Flask(__name__)

## Create bucket session
session = aioboto3.Session()
client = session.client(
    service_name = "s3",
    endpoint_url = os.environ.get("S3_ENDPOINT_URL"),
    aws_access_key_id = os.environ.get("KEY_ID"),
    aws_secret_access_key = os.environ.get("ACCESS_KEY"),
    use_ssl = False,
    verify = False,
)


@app.route("/recognize", methods=["POST"])
def recognize_post():
    if not request.json:
        abort(400)

    ## Get request data
    source = request.json.get("source")
    prefix = request.json.get("prefix")

    ## Check request is ok
    if not source:
        return make_response(jsonify({ "code" : "400", "message" : "No source!" }), 400)
    if not prefix:
        return make_response(jsonify({ "code" : "400", "message" : "No prefix!" }), 400)

    ## Downloading video from url
    print("Start downloading")
    response = urllib.request.urlopen(source)
    byteData = response.read()
    #print (byteData)

    ## Parsing data to parser
    # result = parser(byteData)
    ## or
    # result = parser(responce)
    
    ## Send parser result to bucket
    #asyncio.run(bucket.putVideo(client, f"{prefix}_result.mp4", result["result"]))
    #asyncio.run(bucket.putVideo(client, f"{prefix}_audio.mp4" , result["audio"]))
    #asyncio.run(bucket.putVideo(client, f"{prefix}_video.mp4" , result["video"]))


    ## Save to local storage
    #outFile = open(f"./videos/{prefix}.mp4", 'wb') 
    #shutil.copyfileobj(response, outFile)

    return jsonify({ "code" : "200", "message" : "Ok" })


## Test bucket
@app.route("/recognize", methods=["GET"])
def recognize_get():
    res = asyncio.run(bucket.testConnect(client))
    print(res.decode())
    return jsonify({"body" : res.decode() })


## Run server app
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3444, debug = True)
