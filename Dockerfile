# Use a Python base image (you can choose a specific Python version)
FROM python:3.11.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire directory containing the data into the container
COPY data/ data/

# Copy train.py and test.py into the container
COPY train.py .
COPY test.py .

# Run train.py to generate the model.pkl file
RUN python train.py

# Set the entry point to execute test.py
CMD ["python", "test.py"]