import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# import matplotlib
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

import matplotlib.pyplot as plt

# import seaborn
import numpy as np

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK")


# Fortis stock price
spot_price = 138.90
# Long put

strike_price_long_put = 135

premium_long_put = 4


# Long call

strike_price_long_call = 145

premium_long_call = 3.50


# Stock price range at expiration of the put

sT = np.arange(0.7 * spot_price, 1.3 * spot_price, 1)


def call_payoff(sT, strike_price, premium):
    return np.where(sT > strike_price, sT - strike_price, 0) - premium


payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
# Plot

fig, ax = plt.subplots()

ax.spines["bottom"].set_position("zero")

ax.plot(sT, payoff_long_call, label="Long Call", color="r")

plt.xlabel("Stock Price")

plt.ylabel("Profit and loss")

plt.legend()

plt.show()


# def put_payoff(sT, strike_price, premium):
#       return np.where(sT < strike_price, strike_price - sT, 0) – premium
# payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
# # Plot

# fig, ax = plt.subplots()

# ax.spines['bottom'].set_position('zero')

# ax.plot(sT,payoff_long_put,label='Long Put',color='g')

# plt.xlabel('Stock Price')

# plt.ylabel('Profit and loss')

# plt.legend()

# plt.show()


# payoff_strangle = payoff_long_call + payoff_long_put
# print ("Max Profit: Unlimited")

# print ("Max Loss:", min(payoff_strangle))


# # Plot

# fig, ax = plt.subplots()

# ax.spines['bottom'].set_position('zero')


# ax.plot(sT,payoff_long_call,'--',label='Long Call',color='r')

# ax.plot(sT,payoff_long_put,'--',label='Long Put',color='g')


# ax.plot(sT,payoff_strangle,label='Strangle')

# plt.xlabel('Stock Price')

# plt.ylabel('Profit and loss')

# plt.legend()

# plt.show()


sw = Gtk.ScrolledWindow()
win.add(sw)
# A scrolled window border goes outside the scrollbars and viewport
sw.set_border_width(10)

canvas = FigureCanvas(plt)  # a Gtk.DrawingArea
canvas.set_size_request(800, 600)
sw.add_with_viewport(canvas)

win.show_all()
Gtk.main()
