# Use official Python image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run migrations before starting the server
RUN python manage.py migrate

# Expose port 8000 for Django
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
