FROM mcr.microsoft.com/devcontainers/base:ubuntu
# Install the xz-utils package
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    curl \
    git \
    build-essential

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs

# Install MongoDB
RUN apt-get install -y mongodb

# Install Django
RUN pip3 install django

# Install Flask
RUN pip3 install flask