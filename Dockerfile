FROM python:3.10-slim
# Set working directory inside the container
WORKDIR /app

# Copy only the files from the Docker folder into /app
COPY Docker/ .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask default port
EXPOSE 5000

# Command to run the app
CMD ["python", "medical_plant.py"]