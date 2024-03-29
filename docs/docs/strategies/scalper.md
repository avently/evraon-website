---
title: Scalper
---

You probably know what Scalper strategy means. We buy when spread is huge, we sell right after that
with our profit percent included into the price. If something goes wrong, we do other things.

There are settings you can change:

- min spread for a work. If the spread will be less than the value, the bot will not place an order
- margin from filled orders with purpose Secure. After each filled stop, the bot will
  continue trading only above the price at which the stop was received, or below by a given percent
  multiplied by the number of stops in a row.
  Example: At the price of 100, the bot received a stop. The margin is 1%.
  The bot will NOT buy within 99-100, but only higher or lower. If he buys at 98,
  will receive a stop at 97, it will NOT buy within 95.06-97 (because 97−2×(97÷100) = 95.06)
- type of a grid. The bot places orders by grid and this option indicates
  what type of the grid to use. If Linear, then buy orders will be equidistant from each other.
  If it is exponential, then each next order in the grid will be farther from the previous one
- exponent. If the grid type is set to Exponential, the prices of the second and subsequent
  orders will be calculated using the formula:
  (100 - **x**^(**y** + 1)) \* (bidPrice / 100) - where **x** - exponent, **y** - number of an order
  in the grid (starts from 0)
- margin between orders. If the grid type is Linear, then the prices of the second and
  subsequent orders will be less by the selected percent
- martingale. Increases the amount of the second and subsequent orders by the selected percent.
  Example: martingale is selected as 30%. The minimum order amount is 1 Bitcoin.
  The second order will have (1 + 1 / 100 _ 30%)^1 = 1.3 of Bitcoin.
  The third order will have (1 + 1 / 100 _ 30%)^2 = 1.69 of Bitcoin
- place order with bid/ask price. When the option is enabled, the price of the reply
  order (sell after buy) will be set equal to the ask price.
  In this case, the value of the `take profit percent` option will not be taken into account.

On volatile days, the bot can place hundreds of orders on 5-10 tasks.
If you do not want to use the bot, then simply disable placing orders with the option
`allowed orders` in the task's settings.
