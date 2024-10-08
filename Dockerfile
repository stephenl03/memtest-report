# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/*.py /app
COPY requirements.txt /app

# Create directory for reports
# Install any needed packages specified in requirements.txt
RUN mkdir -p /app/reports \
    && pip install --trusted-host pypi.python.org -r requirements.txt

# Run the command to start gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]
