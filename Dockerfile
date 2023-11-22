FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python ml-pi-dsm5.py

EXPOSE 80

CMD ["gunicorn", "api:app", "--bind", "0.0.0.0:80"]