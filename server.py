import asyncio
import os
import websockets


async def time(websocket, path):

    print('New user, connected')

    filename = r"C:\Users\User\Downloads\Telegram Desktop\debug_scoring.supervisor.log"
    date = 0
    f = open(filename, "r")
    result = f.readlines()[-4:]
    position = f.tell()

    while True:
        try:
            date_1 = os.path.getmtime(filename)

            try:
                new_message = await asyncio.wait_for(websocket.recv(), timeout=2)
                await websocket.send(result)
                print(new_message)
            except asyncio.TimeoutError:
                print('timeout!')

            if date_1 != date:
                date = date_1
                f.seek(position)
                result2 = f.read()
                position = f.tell()
                await websocket.send(result2)
                await asyncio.sleep(1)

        except websockets.ConnectionClosedOK:
            print('connection closed!')
            break


async def start_serv():
    await websockets.serve(time, 'localhost', 12345)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_serv())
    event_loop.run_forever()
