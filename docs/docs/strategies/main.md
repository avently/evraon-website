---
title: Universal settings for strategies
---

Let's talk about strategies. For decades people have tried countless methods of making profit and finding pattens in price movements within stock exchanges. These patterns gradually form a trading strategy. In
essence, a strategy is a set of responses to what is happening in the
market.

Several strategies are built into the program:

- [Scalper](/en/docs/strategies/scalper/)
- [Flash](/en/docs/strategies/flash/)
- [HighLow](/en/docs/strategies/highlow/).

Each of them has its own settings. You can read about them on the
specific strategy page. Now let's look at the settings that work with
all strategies:

- name. To distinguish one from the other, it is better to come up
  with a self-explanatory name. Better yet, put some symbol in front
  of the name itself, for example _\* RISKY SCALPER_. The first character will be shown in the instruments list
  after the name of the instrument itself. This will make it easier for you
  to understand what kind of strategy you have chosen there. After
  all, one set of parameters can be used on dozens of strategies.
- strategy. Here you need to select the desired type of strategy from
  the pop-up list.
- allowed deposit. This is the total amount in Bitcoin for crypto and
  in rubles for Quik, which the bot cannot exceed over all of its
  orders. Of course, you can manually trade while the bot is running
  with whatever amount you chose, but the bot will not be able to
  exceed this limit. Conversion into other currencies is automatic at
  the current exchange rate
- the maximum number of orders. Restriction for the bot, it will not place more orders than you allow
- stop trading after n stops. If the bot has filled the stops n
  times in a row, it will stop trading for some time. Do not neglect
  this option, it could save your balance with poorly thought out
  strategy
- restart trading after n mins. If it was stopped due to several stops
  in a row, then after the selected number of minutes it will continue
  to trade.

Then there are options depending on who the author of the order is: the
bot or a user. What is the difference? If the bot places orders, then
there may be some rules for it, and if you manually - others:

- take profit, in percent. For example, you indicated 1. So, having
  bought at 100, the sale will be set at 101.
- stop loss. In percent. Example: a sell order was placed, it was
  filled, the bot will immediately place a buy stop taking into
  account the stop loss and the average selling price. Please note
  that the market stop order is not supported by the Binance exchange
  for Spot market, so the order is stored locally and placed on the exchange
  as a market order at the right time. This means that if you placed
  an order, and then turned off the bot and did not turn it on again,
  the stop cannot be triggered in any way! For other Binance markets
  and other exchanges, the stop is immediately placed on the exchange.
- delay until order cancellation. Example: you placed a buy order, a
  few seconds passed, no one sold you (or the bot), the order will be
  canceled. If you don't want the order to be cancelled, set it to 0.

#### Moving stops to breakeven

Sometimes it is useful to automatically move stop orders to breakeven as
time passes or when the last price moves away by the required distance.
There are several options for this:

- breakeven percentage. In other words, at what percentage distance to
  rearrange the stop from the entry price of the INITIAL order. That
  is, the order that led to the placement of the stop. Example: bought
  at 100, the stop was set at 99, the breakeven percentage was
  indicated at 1, the stop will move to the price of 101
- distance after which to replace stop into breakeven. This is the distance that the price
  must travel towards your profit, after which the stop will move to
  breakeven. It is counted from the entry price of the INITIAL order.
  To turn off rearrangement to breakeven, specify 0
- force replace stop in breakeven by timeout. This option ignores the
  previous option. Example: set 60 seconds. Regardless of the market
  price, the order will be moved to the breakeven percentage. And it
  can be fulfilled instantly, without even reaching breakeven. Select
  0 to disable this behaviour

#### Increase or decrease in order's price over time

Sometimes your order is not sold after a long time. And it would be
necessary to sell it as soon as possible, but the hope for a rise in prices
is not lost. The bot can lower and lower its orders prices (yours will not
touch), as long as the settings tell it to do this. Let's take an
example: the bot bought at 100, placed a sell at 105. The price does not
go there in any way. A minute passes, the bot cancels the order and
places it at ~ 104. 30 seconds pass, the sale is not executed again.
Rearranges it down by ~ 103. All the same, nothing. Decreases again,
passes again 30 seconds. It is no longer possible to go down, you have
to wait for execution at 103 or stop. Here are the settings you can use
to set this behaviour:

- delay before price change. In the example, this parameter
  is equal to a minute - that is, this is the time before the first
  price decrease
- delay between price changes. In the example, this is 30 seconds.
  That is, after the first price decrease, the bot will take into
  account this value, and not the first one. Every 30 seconds, for
  example.
- change the price by a percentage. How much to change the price from
  the selling price. In the example, this is 1%
- maximum change of a price. If you have already reduced it by n
  percent, then stop doing it and wait for execution or stop order filling. In the
  example, this value is approximately 3%. I write _reduce_, but it
  also works to increase the price when the initial order was for a
  sell, and a profitable one was for a buy.

#### Filters that allow to trade

We don't want the bot to trade all the time. And only when the market
meets our criteria. There are filters for this. With them you limit the
situations in which the bot is allowed to trade. There are two types of
filters: by trading volume and by price of the instrument / market /
main instrument of the exchange:

- volumes per hour and day. Indicate how much the minimum and maximum
  volume should be traded on the exchange in Bitcoins (for crypto) or
  rubles (for Quik) on a working instrument. Example: the strategy
  will be selected on a task with BNBUSDT, the minimum volume is
  100 BTC per hour, the maximum volume is 1000. This means that the
  bot will NOT trade if the volume per hour is less than 100 or more
  than 1000 BITCOINS (or rubles on Quik)
- price differences for different periods. The same as with volumes,
  only with prices. Additionally, there are several timeframes and
  data sources. The source can be price changes from the working
  instrument, the main instrument of the exchange, the average change
  in prices of all exchange instruments. Here, "price change" means
  the percentage value that the price passed during the selected
  period of time. For example, an hour ago the price was 100. Now the
  price is 99. This means that the price has changed by -1% in an
  hour. By _main instrument of the exchange_ I mean BTCUSDT, or XBTUSD, or
  USD000UTSTOM.

Let's summarize. You and the bot can trade simultaneously, and you can
trade on the same instrument at any time in parallel with it. Sometimes
when you think your strategy would not work in a given situation you can
trade on your own. Either way, the chosen strategy settings will help
you automate your actions. For example, you want to place a sell order
at a couple of percent more expensive after a successful purchase and
take into account the stops. Ok, thanks to the strategy settings, you
will get the desired result.

Let's move on to the settings for specific strategies.
