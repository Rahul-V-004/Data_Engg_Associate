# Get Python from offical Python image
FROM python:3.11-slim

# folder inside docker container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py . 

EXPOSE 5000

# we need to run this code which we have copied 
CMD ["python", "app.py"]