# Use an official Python runtime as a parent image
FROM python:3.9

# Environment variable to ensure Python output is unbuffered
ENV PYTHONUNBUFFERED 1

# Create the project directory in the container
RUN mkdir /music_service

# Set the working directory to /music_service
WORKDIR /music_service

# Copy the current directory contents into the container
COPY . /music_service/

# Upgrade pip and install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]