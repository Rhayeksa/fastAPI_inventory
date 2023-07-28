from os import environ

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

env = dotenv_values(".env")

USERNAME = environ.get("INVENTORY_DB_USERNAME") if environ.get(
    "INVENTORY_DB_USERNAME") != None else env["INVENTORY_DB_USERNAME"]
PASSWORD = environ.get("INVENTORY_DB_PASSWORD") if environ.get(
    "INVENTORY_DB_PASSWORD") != None else env["INVENTORY_DB_PASSWORD"]
IP = environ.get("INVENTORY_DB_IP") if environ.get(
    "INVENTORY_DB_IP") != None else env["INVENTORY_DB_IP"]
PORT = environ.get("INVENTORY_DB_PORT") if environ.get(
    "INVENTORY_DB_PORT") != None else env["INVENTORY_DB_PORT"]
DB = environ.get("INVENTORY_DB_INVENTORY") if environ.get(
    "INVENTORY_DB_INVENTORY") != None else env["INVENTORY_DB_INVENTORY"]
URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{IP}:{PORT}/{DB}"


class Base(DeclarativeBase):
    pass


engine = create_engine(url=URI, pool_pre_ping=True)
session = sessionmaker(bind=engine)
session = session()
