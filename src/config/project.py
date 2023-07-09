from os import environ

from dotenv import dotenv_values

env = dotenv_values(".env")

PROJECT = environ.get("PROJECT") if environ.get(
    "PROJECT") != None else env["PROJECT"]
VERSION = environ.get("VERSION") if environ.get(
    "VERSION") != None else env["VERSION"]
DESCRIPTION = environ.get("DESCRIPTION") if environ.get(
    "DESCRIPTION") != None else env["DESCRIPTION"]
