# Daily AI Briefing

A personal AI agent that delivers a daily news briefing to Telegram every morning at 8am.

## What it does

Pulls the latest news across five topic areas, filters and summarises it using Claude, and sends a clean briefing to Telegram. No dashboards, no logins, just a message waiting for you every morning.

**Topics covered:**
- AI and machine learning
- Startups and venture capital
- Growth and GTM
- Creator economy
- Tech

## How it works

1. NewsAPI pulls recent headlines across each topic
2. Claude (Anthropic) reads the articles and writes a structured briefing
3. The briefing is sent to Telegram via bot
4. GitHub Actions runs the whole thing automatically every morning

## Stack

- Python
- Anthropic API (Claude)
- NewsAPI
- Telegram Bot API
- GitHub Actions (scheduling)

## Setup

1. Clone the repo
2. Get API keys for Anthropic, NewsAPI, and Telegram
3. Add them as GitHub Secrets
4. Update the Telegram chat ID to your own
5. Push to GitHub and the Action runs automatically

## Why I built this

I wanted a personalised news briefing tuned to my actual interests, delivered somewhere I'd actually check. Built in one evening as part of my AI portfolio.
