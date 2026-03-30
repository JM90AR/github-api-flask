FROM python:latest
WORKDIR /app
COPY . .
RUN pip install requests flask psycopg2-binary
CMD ["python", "app.py"]