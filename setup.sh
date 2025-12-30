#!/bin/bash

# Berlin Housing DSS - GitHub Setup Script
# This script automates the initial repository setup

echo "🏠 Berlin Housing DSS - GitHub Setup Script"
echo "============================================"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git is not installed. Please install Git first.${NC}"
    echo "   Visit: https://git-scm.com/downloads"
    exit 1
fi

echo -e "${GREEN}✅ Git is installed${NC}"
echo ""

# Get user information
echo "📝 Please provide the following information:"
echo ""

read -p "Your GitHub username: " GITHUB_USERNAME
read -p "Repository name (default: berlin-housing-dss): " REPO_NAME
REPO_NAME=${REPO_NAME:-berlin-housing-dss}

read -p "Your name (for git config): " USER_NAME
read -p "Your email (for git config): " USER_EMAIL

echo ""
echo "📋 Configuration Summary:"
echo "   GitHub Username: $GITHUB_USERNAME"
echo "   Repository Name: $REPO_NAME"
echo "   Your Name: $USER_NAME"
echo "   Your Email: $USER_EMAIL"
echo ""

read -p "Is this correct? (y/n): " CONFIRM
if [[ $CONFIRM != [yY] ]]; then
    echo -e "${YELLOW}Setup cancelled.${NC}"
    exit 0
fi

echo ""
echo "🚀 Starting setup..."
echo ""

# Configure git
echo "⚙️  Configuring Git..."
git config --global user.name "$USER_NAME"
git config --global user.email "$USER_EMAIL"
echo -e "${GREEN}✅ Git configured${NC}"

# Initialize repository if not already done
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    echo -e "${GREEN}✅ Repository initialized${NC}"
else
    echo -e "${YELLOW}⚠️  Git repository already exists${NC}"
fi

# Create .gitignore if it doesn't exist
if [ ! -f .gitignore ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << 'EOF'
# System files
.DS_Store
Thumbs.db
*.swp
*.swo

# Editor files
.vscode/
.idea/
*.sublime-*

# Environment files
.env
.env.local
*.key

# Logs
*.log
npm-debug.log*

# Temporary files
*.tmp
temp/
EOF
    echo -e "${GREEN}✅ .gitignore created${NC}"
fi

# Add all files
echo "📦 Adding files to git..."
git add .
echo -e "${GREEN}✅ Files added${NC}"

# Initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Add Berlin Housing DSS Dashboard"
echo -e "${GREEN}✅ Initial commit created${NC}"

# Set up remote
echo "🔗 Setting up remote repository..."
git branch -M main
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
echo -e "${GREEN}✅ Remote configured${NC}"

echo ""
echo "============================================"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "============================================"
echo ""
echo "📝 Next Steps:"
echo ""
echo "1. Create the repository on GitHub:"
echo "   • Go to: https://github.com/new"
echo "   • Repository name: $REPO_NAME"
echo "   • Make it Public (required for free GitHub Pages)"
echo "   • DO NOT initialize with README (we already have files)"
echo "   • Click 'Create repository'"
echo ""
echo "2. Push your code to GitHub:"
echo "   git push -u origin main"
echo ""
echo "3. Enable GitHub Pages:"
echo "   • Go to: https://github.com/$GITHUB_USERNAME/$REPO_NAME/settings/pages"
echo "   • Source: Deploy from branch 'main'"
echo "   • Folder: / (root)"
echo "   • Click Save"
echo ""
echo "4. Your live site will be at:"
echo "   https://$GITHUB_USERNAME.github.io/$REPO_NAME/Berlin_DSS_Dashboard.html"
echo ""
echo "📚 For detailed instructions, see DEPLOYMENT_GUIDE.md"
echo ""
echo -e "${YELLOW}Note: You'll need a GitHub Personal Access Token to push.${NC}"
echo "   Generate one at: https://github.com/settings/tokens"
echo "   Use it as your password when prompted."
echo ""
echo "🎉 Happy deploying!"
