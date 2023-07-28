from fastapi import APIRouter, Path
from sqlalchemy import delete, select

from src.config.db.inventory import session
from src.model.item import Item
from src.utilities.response import response

router = APIRouter()


@router.delete(
    path="/item/delete/{id}",
    name="remove by id item",
    description="remove by id item",
)
async def remove_by_id(
    id: int = Path()
):
    try:
        query = session.execute(
            select(Item).
            where(Item.id == id)
        ).scalars().fetchall()
        if len(query) < 1:
            return await response(code=404, message="ID not found")

        session.execute(
            delete(Item).
            where(Item.id == id)
        )

        session.commit()
        return await response(code=200)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
