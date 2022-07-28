# CRYPTOCURRENCIES CHECKER

## DESCRIPTION
Telegram bot to track the prices of cryptocurrencies and the current balance on the binance account. 
Tracking occurs by the difference of the entered value and the bot will report on the growth or fall of the currency.

Stack: aiogram, aioschedule, PostgreSQL, python-binance

## How to use this project: 

Cloning the project

> git clone https://github.com/DarkStussy/cryptocurrencies_checker.git

> cd cryptocurrencies_checker

Create virtual environment

> python -m virtualenv venv

Activate virtual environment

WINDOWS:

> venv\Scripts\activate

LINUX:

> source venv/bin/activate

Installing the required dependencies

> pip install -r requirements.txt


Create an .env file at the root of the project and paste:

  <sub>BOT_TOKEN=your-bot-token
  PG_HOST=postgres-host(default:localhost)
  PG_USERNAME=postgres-username
  PG_PASSWORD=postgres-password
  PG_DATABASE=postgres-database
  BINANCE_API_KEY=binance-api-key
  BINANCE_API_SECRET=binance-api-secret</sub>
  
And run the bot: 

> python app.py

READY! :)
