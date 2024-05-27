# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container at /usr/src/app
COPY run_code.py .

# Command to run on container start
CMD ["python", "run_code.py"]
