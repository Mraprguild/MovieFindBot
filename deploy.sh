#!/bin/bash

# Quick Deploy Script for Telegram Movie Bot
set -e

echo "🎬 Telegram Movie Bot - Quick Deploy"
echo "=================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please configure your API keys in .env file:"
    echo "   nano .env"
    echo ""
    echo "Required:"
    echo "   - TELEGRAM_BOT_TOKEN (from @BotFather)"
    echo "   - OMDB_API_KEY (from omdbapi.com)"
    echo ""
    read -p "Press Enter after configuring .env file..."
fi

# Build and start the services
echo "🔨 Building and starting services..."
docker-compose up -d --build

echo ""
echo "✅ Bot is now running!"
echo ""
echo "📊 Web Dashboard: http://localhost:5000"
echo "📱 Check logs: docker-compose logs -f"
echo "🛑 Stop bot: docker-compose down"
echo ""
echo "🎉 Your Telegram Movie Bot is ready!"