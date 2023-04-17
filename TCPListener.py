import asyncio
from asyncore import loop
import socket
from Parser import *
from GILogger import *
from datetime import datetime


async def receiver(conn):
    # time1 = datetime.now()
    loop = asyncio.get_event_loop()
    line = (await loop.sock_recv(conn, 1024)).decode('utf8')
    return line


async def sender(conn, result):
    # time1 =datetime.now()
    loop = asyncio.get_event_loop()
    await loop.sock_sendall(conn, result.encode('utf8'))
    # time2 = datetime.now()
    # print("Send Time ....",time2-time1)


async def process(conn):
    # async def process(reader, writer):
    loop = asyncio.get_event_loop()
    # line = ""
    all_line = ""
    while 1:
        print("awaiting for data")
        line = await receiver(conn)
        if len(line) > 1:
            all_line += str(line)
            if '***' in all_line:
                all_line = all_line.rstrip(all_line[-3])
                #all_line1 = all_line.replace("****", "")
                break
            # time1 =datetime.now()
    if len(all_line) > 1:
        app_log.info("received"+str(all_line))
        result = data_extractor(all_line)
        print(f"received {all_line}")
        await sender(conn, result)
        print(f"sent {result}")
        app_log.info("Sent to client " + str(result))


async def new_session(conn):
    loop = asyncio.get_event_loop()
    print("new session started")
    try:
        await asyncio.wait_for(process(conn), timeout=10)
        print("looping")
    except asyncio.TimeoutError as te:
        print(f'time is up!{te}')
        app_log.exception(te)
    finally:
        conn.close()
        print("writer closed")


async def a_main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(3000)
        server.setblocking(False)
        print("Server started listening")
        loop = asyncio.get_event_loop()
        while 1:
            conn, adres = await loop.sock_accept(server)
            loop.create_task(new_session(conn))
    except Exception as e:
        app_log.exception(e)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 31051
    asyncio.run(a_main())
