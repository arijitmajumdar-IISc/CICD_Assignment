# Use a Python base image (you can choose a specific Python version)
FROM python:3.11.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy train.py and test.py into the container
COPY train.py .
COPY test.py .

# Set the entry point to execute train.py followed by test.py
ENTRYPOINT ["python", "train.py"]