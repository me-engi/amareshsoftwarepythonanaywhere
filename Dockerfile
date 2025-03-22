# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y default-mysql-client

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements_live.txt

RUN pip install gunicorn

# Expose port 8000
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project_name.wsgi:application"]
