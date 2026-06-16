FROM python:3.12-slim

WORKDIR /app

# Install build dependencies for scientific libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Flask default port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
