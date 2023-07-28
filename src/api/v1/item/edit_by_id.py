from datetime import datetime

from fastapi import APIRouter, Body, Path
from sqlalchemy import select, update

from src.config.db.inventory import session
from src.model.item import Item
from src.utilities.response import response

router = APIRouter()


@router.put(
    path="/item/edit/{id}",
    name="edit by id item",
    description="edit by id item"
)
async def edit_by_id(
    id: int = Path(...),
    name: str = Body(""),
    quantity: str = Body(""),
    description: str = Body(""),
):
    try:
        query = session.execute(
            select(Item).
            where(Item.id == id)
        ).scalars().fetchall()
        if len(query) < 1:
            return await response(code=404, message="ID not found")

        query = session.execute(
            select(Item).
            where(Item.id == id)
        ).scalars().first()
        name = name if name != "" else query.name  # type: ignore
        quantity = quantity if quantity != "" else query.quantity  # type: ignore
        description = description if description != "" else query.description  # type: ignore

        session.execute(
            update(Item).
            where(Item.id == id).
            values(
                name=name,
                quantity=int(quantity),
                description=description,
                updated_at=datetime.now(),
            )
        )

        session.commit()
        return await response(code=200)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
