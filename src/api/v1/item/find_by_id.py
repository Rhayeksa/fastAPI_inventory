from fastapi import APIRouter, Path
from sqlalchemy import select

from src.config.db.inventory import session
from src.model.item import Item
from src.utilities.response import response

router = APIRouter()


@router.get(
    path="/item/{id}",
    name="find by id item",
    description="find by id item"
)
async def find_by_id(
    id: int = Path(...),
):
    try:
        data = session.execute(
            select(Item).
            where(Item.id == id)
        ).scalars().first()

        return await response(code=200, data=data)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
