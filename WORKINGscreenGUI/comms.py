import asyncio
import websockets

async def connect_to_server():
    uri = "ws://192.168.4.2:81"  # WebSocket server address on NodeMCU
    async with websockets.connect(uri) as websocket:
        # Send and receive data using websocket.send() and websocket.recv() methods
        await websocket.send("Hello from Kivy app!")
        response = await websocket.recv()
        print(f"Received from server: {response}")
        # ... handle incoming data and send updates to Kivy UI as needed

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_server())

