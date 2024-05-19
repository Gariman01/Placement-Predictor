# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install libgomp1 for LightGBM
RUN apt-get update && apt-get install -y libgomp1

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME placement_predictor

# Run api.py when the container launches
CMD ["python", "api.py"]