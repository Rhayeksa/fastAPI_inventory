from datetime import datetime

from fastapi import APIRouter, Body
from sqlalchemy import insert, select

from src.config.db.inventory import session
from src.model.item import Item
from src.utilities.response import response

router = APIRouter()


@router.post(
    path="/item/add",
    name="add item",
    description="add item"
)
async def add(
    name: str = Body(""),
    quantity: str = Body(""),
    description: str = Body(""),
):
    try:
        query = session.execute(
            select(Item).
            where(Item.name == name)
        ).scalars().fetchall()
        if len(query) > 0:
            return await response(code=409, message="Name already exist")

        if "" in [name, quantity]:
            return await response(code=400, message="Name and quantity is required")

        session.execute(
            insert(Item).
            values(
                name=name,
                quantity=int(quantity),
                description=description,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        )

        session.commit()
        return await response(code=201)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
