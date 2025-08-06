#!/bin/bash

# Telegram Movie Bot - Docker Build Script
set -e

echo "🎬 Building Telegram Movie Bot Docker Image..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "📝 Please copy .env.example to .env and configure your API keys:"
    echo "   cp .env.example .env"
    echo "   nano .env"
    echo ""
fi

# Build the Docker image
echo "🔨 Building Docker image..."
docker build -t telegram-movie-bot:latest .

echo "✅ Docker image built successfully!"
echo ""
echo "🚀 To run the bot:"
echo "   docker-compose up -d"
echo ""
echo "📊 To view the dashboard:"
echo "   Open http://localhost:5000 in your browser"
echo ""
echo "📱 To check logs:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 To stop the bot:"
echo "   docker-compose down"