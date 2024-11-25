import asyncio
import time

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse


app = FastAPI()


async def event_stream():
    while True:
        await asyncio.sleep(1)
        yield f"data: Current time is {time.ctime()}\n\n"


@app.get("/events")
async def events():
    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/")
async def index():
    html_content = 'test'
    return HTMLResponse(content=html_content)
