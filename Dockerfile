# Step 1: Use a newer Python base image (assuming compatible)
FROM python:3.11-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 4: Install dependencies for Allure CLI
RUN apt-get update && apt-get install -y wget unzip

# Install OpenJDK 11 from an alternative source
RUN apt-get update && \
    apt-get install -y wget curl && \
    curl -qO https://adoptium.net/tempurin/8/hotspot/linux/x64/jdk/11.0.17/jdk-11.0.17-hotspot-linux-x64.tar.gz | tar -xzf - /usr/local/java

# Step 5: Copy the rest of your application code
COPY . .

# Step 6: Command to run your tests
CMD ["pytest", "--alluredir=reports/"]