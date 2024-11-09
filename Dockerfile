# Use the official Python 3.12 image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available
EXPOSE 5000

# Run flask
CMD ["python", "app.py"]
