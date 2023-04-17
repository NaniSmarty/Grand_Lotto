import asyncio
import socket
import methods


async def process(conn):
#async def process(reader, writer):
    loop = asyncio.get_event_loop()
    line = ""
    while True:
        if line == 'quit':
            print("breaking loop")
            break
        else :
            print("awaiting for data")
            line = (await loop.sock_recv(conn, 255)).decode('utf8')
            result = methods.login(line)
            line = ""
            print(f"received {result}")
            await loop.sock_sendall(conn, result.encode('utf8'))
            print(f"sent {result}")
    


async def timeout(task: asyncio.Task, duration):
    print("timeout started")
    await asyncio.sleep(duration)
    print("client unresponsive, cancelling")
    task.cancel()
    print("task cancelled")


async def new_session(conn):
    loop = asyncio.get_event_loop()
    print("new session started")
    try:
        await asyncio.wait_for(process(conn), timeout=20)
        print("looping")
    except asyncio.TimeoutError as te:
        print(f'time is up!{te}')
    finally:
        conn.close()
        print("writer closed")


async def a_main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1000)
    server.setblocking(False)
    print("Server started listening")
    loop = asyncio.get_event_loop()
    while True:
        conn , adres = await loop.sock_accept(server)
        loop.create_task(new_session(conn))


if __name__ == '__main__':
    host ='192.168.10.134'
    port = 9004
    asyncio.run(a_main())