# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Define the command to run when the container starts
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
