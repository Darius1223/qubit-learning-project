FROM python:3.8-slim

WORKDIR /backend

COPY requirements/prod.txt requirements/prod.txt
COPY requirements/base.txt requirements/base.txt

RUN pip install -r requirements/prod.txt

COPY . .

RUN useradd -ms /backend larisa

USER larisa

CMD ["scripts/startup.sh"]