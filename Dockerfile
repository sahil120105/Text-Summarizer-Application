FROM python:3.13-slim-bookworm

# Install basic build tools that some local dev packages (like editable installs) might need
RUN apt-get update -y && \
    apt-get install -y gcc git && \
    apt-get clean

WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install your heavy GPU and ML dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run Uvicorn with hot-reloading enabled for local development
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]