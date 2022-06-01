import asyncio
import datetime
import os
import random
import websockets


async def time(websocket, path):
    # while True:
    # now = datetime.datetime.utcnow().isoformat() + 'Z'
    # await websocket.send(now)
    # await asyncio.sleep(random.random() * 5)

    # word = '[CHAT]'  # Word there we search
    # f = open('LOG.log', 'r')  # File where searching word
    # while True:  # infinite cycle
    #     text = f.read().split('\n')  # Reading a file and splitting it by delimiter ('\n')
    #     for i in text:  # Searching word
    #         if word in i:  # If i have word
    #             print(i)  # Printing word
    #     time.sleep(1)
    print('New user, connected')

    filename = r"C:\Users\User\Downloads\Telegram Desktop\debug_scoring.supervisor.log"
    date = 0
    f = open(filename, "r")
    result = f.readlines()[-4:]
    position = f.tell()

    while True:
        new_message = await websocket.recv()
        print(new_message)
        if new_message == 'is_open':
            await websocket.send(result)
        date_1 = os.path.getmtime(filename)
        if date_1 != date:
            print('user, is loop')
            date = date_1
            f.seek(position)
            result2 = f.read()
            position = f.tell()
            f.close()
            await websocket.send(result2)
            await asyncio.sleep(random.random() * 3)
        # else:
        #     f = open(filename, "r")
        #     result = f.readlines()[-4:]
        #     position = f.tell()
        #     f.close()
        #     await websocket.send({
        #         'result': result,
        #         'type': '2'
        #     })
        #     await asyncio.sleep(random.random() * 3)


async def start_serv():
    await websockets.serve(time, 'localhost', 12345)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_serv())
    event_loop.run_forever()

# start_server = websockets.serve(time, '127.0.0.1', 12345)
#
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
