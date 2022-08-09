import asyncio
import imp
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        logging.info(f"message: {message}")