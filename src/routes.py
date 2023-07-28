from src.api.root import router
from src.api.v1.index import router as item

routes = [
    router,
    item,
]
