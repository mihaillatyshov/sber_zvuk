from time import sleep
from collections import deque
from tornado.ioloop import IOLoop
import asyncio
import datetime


async def getData():
	await asyncio.sleep(1)
	print(datetime.datetime.now())
	return "Data"


async def hello():
	data = await getData()
	print(datetime.datetime.now())
	print(data)
	return "test"

		


while True:
	print(datetime.datetime.now(), "hello")
	res = asyncio.run(hello())
	print(res)
	sleep(2)
	


