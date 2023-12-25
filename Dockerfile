# Use the official Python image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1


RUN apt-get update && \
    apt-get install -y libsystemd-dev
ENV PKG_CONFIG_PATH /usr/lib/pkgconfig:/usr/share/pkgconfig

       
# Copy the requirements file
COPY requirements.txt /app/

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && python -m pip cache purge
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
