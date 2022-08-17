import asyncio
import imp
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        logging.info(f"message: {message}")

async def consume(hostname: str, port: int) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)