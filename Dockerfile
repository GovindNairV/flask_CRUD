FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]
