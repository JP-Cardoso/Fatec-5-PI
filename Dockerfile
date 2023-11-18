FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ml-pi-credit.py .
RUN python ml-pi-credit.py

COPY api.py .

# CMD ["python", "api.py"]
CMD ["gunicorn", "api:app", "--bind", "0.0.0.0:5000"]
