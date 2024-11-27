import uuid
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

directory = Path(__file__).parent.parent

app.mount("/static", StaticFiles(directory=f"{directory}/static"), name="static")

templates = Jinja2Templates(directory=f"{directory}/templates")


async def event_stream(data: int | str):
    yield
    while data:
        if data == "STOP":
            break
        data = yield f"⏱: {data} sec"
    yield "🚀"


@app.websocket("/events")
async def events(websocket: WebSocket, session_id: str = Query()):
    await websocket.accept(
        headers=[("session_id".encode(), session_id.encode())]
    )
    try:
        counter = 5
        gen = event_stream(counter)
        await gen.asend(None)
        send_text = await gen.__anext__()
        while counter >= 0:
            await websocket.send_json({"text": send_text})
            received_text = await websocket.receive_json()
            print(received_text)
            counter -= 1
            send_text = await gen.asend(counter)
        await gen.asend("STOP")
    except StopAsyncIteration:
        pass
    except WebSocketDisconnect:
        await websocket.close()


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        headers={"session_id": str(uuid.uuid4())},
    )


if __name__ == '__main__':
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
