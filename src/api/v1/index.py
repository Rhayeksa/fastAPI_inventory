from fastapi import APIRouter

from src.api.v1.item.add import router as add_item
from src.api.v1.item.edit_by_id import router as edit_by_id_item
from src.api.v1.item.find_all import router as find_all_item
from src.api.v1.item.find_by_id import router as find_by_id_item
from src.api.v1.item.remove_by_id import router as remove_by_id_item

router = APIRouter(
    prefix="/v1",
    tags=["V1"]
)

routes = [
    add_item,
    find_by_id_item,
    find_all_item,
    edit_by_id_item,
    remove_by_id_item,
]

for route in routes:
    router.include_router(router=route)
