#!/bin/bash

# WordPress MCP Plugin Setup Script
# Configures .env file with credentials from macOS Keychain

echo "WordPress MCP Plugin Setup"
echo "=========================="
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Error: .env file not found. Copy .env.template to .env first."
    exit 1
fi

# Try to fetch password from Keychain
echo "Retrieving WordPress application password from Keychain..."
PASSWORD=$(security find-generic-password -a "admin" -s "wordpress-mcp" -w 2>/dev/null)

if [ -z "$PASSWORD" ]; then
    echo "Password not found in Keychain under 'wordpress-mcp'."
    echo ""
    echo "Manual setup:"
    echo "1. Open Keychain Access (Applications > Utilities > Keychain Access)"
    echo "2. Search for your WordPress password or 'claude'"
    echo "3. Copy the password"
    echo "4. Edit .env and paste it in WORDPRESS_PASSWORD="
    echo ""
    read -p "Enter WordPress application password: " PASSWORD
fi

# Update .env file with password
if [ ! -z "$PASSWORD" ]; then
    # Use sed to replace the password line (handle special characters)
    sed -i '' "s/^WORDPRESS_PASSWORD=.*/WORDPRESS_PASSWORD=$PASSWORD/" .env
    echo "✓ Password configured in .env"
    echo ""
    echo "Setup complete! Your .env file is ready."
    echo "Make sure .env is in .gitignore and never commit it."
else
    echo "Error: No password provided."
    exit 1
fi
