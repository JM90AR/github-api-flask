FROM python:latest
WORKDIR /app
COPY . .
RUN pip install requests flask
CMD ["python", "app.py"]