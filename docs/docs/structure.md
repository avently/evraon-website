---
title: Structure
---

#### After the start some files will be created inside a directory with the jar file:

- keystore.p12 - certificate is needed for making a secure connection between the server and clients
- configs.json - file contains configuration for strategies you'll use
- notifications.json - notification settings
- profiles.json - profiles with exchanges' data like API keys, fee, etc
- server.json - server settings
- subscription.json - stores your paid subscription's key
- tasks.json - tasks for the bot and manual trading
- telegram.json - Telegram bot's settings.

#### Directories:

- logs - if bot was setup to save logs in file this directory will hold log files. Old files will be automatically removed
- sessions - stores open orders, closed orders, balance history. Balance history shows your Profit and Loss after trades by day
- demo - stores information about demo exchange that is made by the app. It contains orders, virtual wallets and positions.
