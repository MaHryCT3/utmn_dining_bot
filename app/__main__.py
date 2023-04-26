import asyncio

from dotenv import load_dotenv

from app.entrypoint import start_polling

load_dotenv('.env')


loop = asyncio.get_event_loop()
loop.run_until_complete(start_polling())
