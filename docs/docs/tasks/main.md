---
title: Main settings of a task
---

The task is something that holds your intention about a trading instrument. It contains the following parts:

- status of the task. Is it enabled or not? If not, the bot will not track any info about the instrument
  (orders, positions, etc)
- profile. Profile contains an exchange name, API keys for the exchange and some other things
- symbol of the instrument (ticker). For example, BTCUSDT
- strategy and its settings. Without the strategy and without the task, it's impossible to trade. The settings for the task
  hold many options, we'll talk about them later
- wallet. For Quik it's client code. For Binance the wallet can be Spot, Margin, Futures (perp.), Futures (other).
  For Demo subprofile it's always Demo
- allowed orders. This option is only for the bot. You can allow buy orders only, sell orders only, all of them, or
  non of them. If you choose to disable everything the bot will only react on your orders (will place take profit and
  stop orders, will replace them based on other options, etc). Read more in a strategies description
- min order amount. Bot uses it to calculate the right amount for the order. Don't forget to choose the right currency
  for this amount. THe bot will do the rest - it will convert the currency to ticker's lot currency
- notes. Just a place for your notes, nothing special

So, let's summarize. The file named `tasks.json` contains your tasks. You can read it if you use a server on your computer.
Or you can see all tasks withing the app. You can easily change any task via the app. Than the app will know what
you want to do with the instrument and how to react on market situation, what strategy to use, on what exchange to trade
and how to calculate a price of an order.

Let's go to the next page.
