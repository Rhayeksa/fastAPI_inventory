FROM python:3.11.4

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./src /code/src
COPY ./main.py /code/main.py

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9001"]
