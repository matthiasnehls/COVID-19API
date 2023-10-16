FROM ubuntu:22.04
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential python3-dev python3-pip -y
RUN python3 -m pip install fastapi[all] aiohttp[speedup] bs4[speedup] fastapi_plugins scrapy aioredis ujson lxml
RUN mkdir -p /opt/gc-api-breaches
COPY . /opt/gc-api-breaches
WORKDIR /opt/gc-api-breaches
EXPOSE 80
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "run:app"]