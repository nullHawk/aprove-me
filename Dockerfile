FROM python:3.9-slim

WORKDIR /code
COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860
CMD ["python", "app.py"]
