---
title: Flash
---

The strategy is based on an idea that a price often falls (or rises) quickly, but then moves backward. So we can get ready to this event and to place an order before this happens, then to wait until order executes, then to place an opposite order and to wait until it be filled too. Almost everyone trades like this by hand. We can automate it.

Options:
- buy under % from last price. Will place an order using this price: last price - selected % of it. Then will wait before successful fill or will replace it based on the setting below
- to min price before replace. When last price drops by this percent bot will wait some time and then will replace the order
- before order's price editing on price drop. Will move the order below if the price falls rapidly. If not, order will be successfully bought
- before order moving to top. Will move the order above if price is increasing after n seconds from buy order's fill
- add % from price per hour. Will add to sell price: this percent * percent change of instrument per hour
- add % from daily change of all instruments. Will add to sell price: this percent * percent change of all instruments per hour
- add % from main exchange's instrument change. Will add to sell price: this percent * percent change of the main instrument of exchange per hour
- place order using bid/ask price. Price will be made using ask/bid price an instrument. Take profit price from main settings will not be used.