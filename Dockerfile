FROM python:3.11.4
# FROM ubuntu:22.04
# RUN apt update
# RUN apt install software-properties-common -y
# RUN add-apt-repository ppa:deadsnakes/ppa
# ENV DEBIAN_FRONTEND noninteractive
# ARG DEBIAN_FRONTEND=noninteractive
# RUN apt install python3.11 python3.11-venv -y
# RUN apt install python3-pip -y

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./src /code/src

# RUN python3.11 -m venv ./.venv
# RUN source ./.venv/bin/activate
# CMD [ "source", "./.venv/bin/activate" ]
# EXPOSE 8000
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
