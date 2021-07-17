---
title: Highlow
---

This strategy works on the buy low, sell high principle. As soon as the
bot realizes that the market is falling into the abyss, updating the
lows for a certain period, it waits for a reversal at the bottom
and places a buy order. This also works in the opposite direction - as
soon as the market makes new highs, waits for a reversal and
sells. Simultaneously with entering the market, stop and take-profit
are placed (orders that will close the position with a profit).

In order for the bot to make a decision to enter the market, it needs to
wait until the settings you specify are met. Due to the differences in
certain trading instruments, it is better to create one set of
parameters for one instrument.

The strategy is based on the idea that when the overwhelming majority of
people on lows are looking to sell at the market, then the market
reversal is already close. And at some point, the balance of power will
change - there will be more buyers in the market and the price will
bounce. Therefore, it is necessary to choose such settings, at which we
are guaranteed to get a reversal.

In total, what the bot does:

-   waiting for the percentage of trades with the trend to be suitable
-   waiting for extremum updates
-   detects a reversal and enters
-   puts stop, then take-profit
-   is waiting
-   if the stop has been fulfilled, then it removes the take and then
    either restarts or waits for the extremums to be updated again
-   if the price moves a distance *distance after which to replace stop in breakeven*, then it rearranges the order
-   if the stop is executed, then it removes the take and then either
    restarts or waits for the extremums to be updated again
-   if the take is fulfilled, then it removes the stop and everything
    starts again.

Here's what you can customize:

-   the number of trades for analysis. Example: 300 was selected. That
    is, every second (depending on the settings of *profile*, option
    *delay between requests*) the last 300 trades will be
    analyzed and how many of them were along the trend and how many were
    against the trend.
-   percentage of trades with the trend. Example: 98.4%. This means
    that when 296+ out of 300 trades follow the trend (selling when the
    price is falling, buying when the price is rising), the bot will
    wait for the update of the lows or highs
-   number of candles to analyze. Determines how many candles on
    the chart to take to calculate the minimum and maximum prices
-   candles' timeframe. How much is in one candle - 1 minute,
    5 minutes, hour, day. The larger the timeframe, the less frequent
    trades will be
-   waiting time for a turn. How many seconds the bot will wait for a
    reversal before being ready to enter the market. Example: set 4
    seconds, the price falls, the number of trades with the trend is a
    suitable amount, the minimum is updated, the bot starts to sort all
    trades into "candles" with a duration of one second. Takes a 4 second
    candle * the number of crossing break percentages. Determines
    whether the market began to reverse within these few seconds or not.
    If the market started, the bots enters into the deal. Please note that the number
    of second candles = option value * percentage of price distance from
    high/low. Example: the price went out for a minimum of 2.5%
    compared to the previous minimum. 4 seconds (your choice) * 2.5% =
    10 candles per one second. This approach helps to catch the best prices even
    with the strongest XBTUSD moves at 5% per minute. After all, the
    stronger the movement, the longer the price will be at extremes and
    the more difficult it is to determine the reversal
-   enter using limit order. On some exchanges, the commission
    will be paid to you, not by you, when you enter with a limit. Price may
    not return to your lonely limit (ideally, a correct entry will
    ensure that the price will not return). But if suddenly the price
    returns, then you will save on commissions and get a better entry
    price. With certain settings, this approach may be preferable to
    market entry
-   distance to entry price. If a limit
    entry is selected, the value of this option moves the entry price
    away from the price at which the bot determined the beginning of the
    reversal. Example: at a price of 100, the bot determined that the
    market is turning and that it is possible to enter. Counts this
    percentage of the bid/ask price (when buying / selling), places a
    limit order, places stop and take
-   reenter again n times after stop. When a bot enters a position, the market
    may roll back a little, and then want to take out the stops of new
    arrivals, and only then really roll back a lot. This phenomenon
    often occurs, so you may decide that the bot needs to re-enter after
    the stop. But it's not stupid to enter the market at the same
    moment: he waits for a reversal again. Example: the price is 100,
    the bot entered at 101, the price walked around 101.5-101.7, but did
    not reach your take. Then it went down, executed your stop at 100.8,
    continued to fall to 100.1 without updating the minimum, the bot
    waited for a reversal and entered the trade again. This will be
    repeated as long as the number of consecutive stops allowed will
    allow (otherwise the bot will take a break), or as long as the
    number of restarts will allow. I highly recommend NOT allowing
    re-enter many times.
