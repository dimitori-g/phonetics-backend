FROM python:3.11-alpine

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN apk add build-base libffi-dev

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]