FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
COPY script_create_examples.py .
RUN python script_create_examples.py
EXPOSE 8000

CMD ["python", "main.py"]
