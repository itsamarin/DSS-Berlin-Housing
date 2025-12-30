@echo off
REM Berlin Housing DSS - GitHub Setup Script for Windows
REM This script automates the initial repository setup

echo ======================================
echo Berlin Housing DSS - GitHub Setup
echo ======================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed. Please install Git first.
    echo Visit: https://git-scm.com/downloads
    pause
    exit /b 1
)

echo [OK] Git is installed
echo.

REM Get user information
echo Please provide the following information:
echo.

set /p GITHUB_USERNAME="Your GitHub username: "
set /p REPO_NAME="Repository name (default: berlin-housing-dss): "
if "%REPO_NAME%"=="" set REPO_NAME=berlin-housing-dss

set /p USER_NAME="Your name (for git config): "
set /p USER_EMAIL="Your email (for git config): "

echo.
echo Configuration Summary:
echo   GitHub Username: %GITHUB_USERNAME%
echo   Repository Name: %REPO_NAME%
echo   Your Name: %USER_NAME%
echo   Your Email: %USER_EMAIL%
echo.

set /p CONFIRM="Is this correct? (y/n): "
if /i not "%CONFIRM%"=="y" (
    echo Setup cancelled.
    pause
    exit /b 0
)

echo.
echo Starting setup...
echo.

REM Configure git
echo Configuring Git...
git config --global user.name "%USER_NAME%"
git config --global user.email "%USER_EMAIL%"
echo [OK] Git configured
echo.

REM Initialize repository if not already done
if not exist .git (
    echo Initializing Git repository...
    git init
    echo [OK] Repository initialized
) else (
    echo [WARNING] Git repository already exists
)
echo.

REM Create .gitignore if it doesn't exist
if not exist .gitignore (
    echo Creating .gitignore...
    (
        echo # System files
        echo .DS_Store
        echo Thumbs.db
        echo *.swp
        echo *.swo
        echo.
        echo # Editor files
        echo .vscode/
        echo .idea/
        echo *.sublime-*
        echo.
        echo # Environment files
        echo .env
        echo .env.local
        echo *.key
        echo.
        echo # Logs
        echo *.log
        echo npm-debug.log*
        echo.
        echo # Temporary files
        echo *.tmp
        echo temp/
    ) > .gitignore
    echo [OK] .gitignore created
    echo.
)

REM Add all files
echo Adding files to git...
git add .
echo [OK] Files added
echo.

REM Initial commit
echo Creating initial commit...
git commit -m "Initial commit: Add Berlin Housing DSS Dashboard"
echo [OK] Initial commit created
echo.

REM Set up remote
echo Setting up remote repository...
git branch -M main
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
echo [OK] Remote configured
echo.

echo ======================================
echo [SUCCESS] Setup Complete!
echo ======================================
echo.
echo Next Steps:
echo.
echo 1. Create the repository on GitHub:
echo    - Go to: https://github.com/new
echo    - Repository name: %REPO_NAME%
echo    - Make it Public (required for free GitHub Pages)
echo    - DO NOT initialize with README (we already have files)
echo    - Click 'Create repository'
echo.
echo 2. Push your code to GitHub:
echo    git push -u origin main
echo.
echo 3. Enable GitHub Pages:
echo    - Go to: https://github.com/%GITHUB_USERNAME%/%REPO_NAME%/settings/pages
echo    - Source: Deploy from branch 'main'
echo    - Folder: / (root)
echo    - Click Save
echo.
echo 4. Your live site will be at:
echo    https://%GITHUB_USERNAME%.github.io/%REPO_NAME%/Berlin_DSS_Dashboard.html
echo.
echo For detailed instructions, see DEPLOYMENT_GUIDE.md
echo.
echo Note: You'll need a GitHub Personal Access Token to push.
echo    Generate one at: https://github.com/settings/tokens
echo    Use it as your password when prompted.
echo.
echo Happy deploying!
echo.
pause
