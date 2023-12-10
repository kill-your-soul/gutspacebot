FROM python:3.10 as builder
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.10-slim-buster
WORKDIR /app
RUN apt-get update && \
    apt-get install -y libpq-dev

COPY . .
COPY --from=builder /app/wheels /app/wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /app/wheels/*
WORKDIR /app/src

CMD [ "python3", "bot.py"]
