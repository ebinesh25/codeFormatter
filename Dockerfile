# Use debian:bullseye-slim as the base image
FROM debian:bullseye-slim

# Set environment variables to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    gnupg \
    clang-format \
    php-cli \
    --no-install-recommends

# Install Node.js 20.x
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Black for Python formatting
RUN pip3 install black

# Install Prettier for JavaScript, HTML, CSS, and JSON formatting
RUN npm install -g prettier

# Install PHP-CS-Fixer
RUN curl -L https://cs.symfony.com/download/php-cs-fixer-v3.phar -o php-cs-fixer && \
    chmod +x php-cs-fixer && \
    mv php-cs-fixer /usr/local/bin/php-cs-fixer

# Install SQL Formatter CLI
RUN npm install -g sql-formatter-cli

# Verify installations
RUN black --version && \
    prettier --version && \
    clang-format --version && \
    php-cs-fixer --version && \
    sql-formatter-cli --version

# Create and set a volume for code
VOLUME /workspace
WORKDIR /workspace
    
# Set entrypoint to bash
CMD ["/bin/bash"]