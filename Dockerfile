FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ml-pi-dsm5.py .

COPY credit.csv .

COPY mapper_data.py  .

RUN python ml-pi-dsm5.py

COPY api.py .

# CMD ["python", "api.py"]
CMD ["gunicorn", "api:app", "--bind", "0.0.0.0:5000"]