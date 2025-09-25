#!/bin/bash

# Update package lists
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install Black for Python formatting
pip3 install black

# Install Node.js and npm (required for Prettier)
sudo apt install -y nodejs npm

# Install Prettier for JavaScript, HTML, CSS, and JSON formatting
sudo npm install -g prettier

# Install clang-format for C, C++, and Java formatting
sudo apt install -y clang-format

# Install PHP and PHP-CS-Fixer
sudo apt install -y php-cli
curl -L https://cs.symfony.com/download/php-cs-fixer-v3.phar -o php-cs-fixer
chmod +x php-cs-fixer
sudo mv php-cs-fixer /usr/local/bin/php-cs-fixer

# Install SQL Formatter CLI
sudo npm install -g sql-formatter-cli

# Verify installations
echo "Installed versions:"
black --version
prettier --version
clang-format --version
php-cs-fixer --version
sql-formatter-cli --version

echo "All required formatters have been installed."
