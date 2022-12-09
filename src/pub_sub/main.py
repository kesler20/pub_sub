from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
try:
    import pub_sub.mqtt_client as mqtt_client
except ModuleNotFoundError:
    import src.pub_sub.mqtt_client as mqtt_client

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["."],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url='/docs')
    return response


@app.post('/mqtt/connection_status')
async def handle_upload():
    mqtt_client.MQTTClient
    return {"connection_status": 200}
