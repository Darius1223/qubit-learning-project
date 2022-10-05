FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements/prod.txt

CMD ["scripts/startup.sh"]