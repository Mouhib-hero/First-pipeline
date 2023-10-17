# Using the right version of python
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /

# Copy all files to the container
COPY . .

# Expose the port that the application will run on
EXPOSE 5000

# Set the command to run the application using Flask development server
CMD ["python", "app.py"]
