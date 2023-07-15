from fastapi import FastAPI
from src.routes import routes
# from src.config.project import PROJECT, VERSION, DESCRIPTION

app = FastAPI(
    # title=PROJECT or "FastAPI",
    # description=DESCRIPTION or "FastAPI",
    # version=VERSION or "0.1.0",
)

for route in routes:
    app.include_router(route)
