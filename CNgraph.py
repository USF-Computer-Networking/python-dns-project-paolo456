import pygal
from pygal.style import Style

custom_style = Style(
  colors=('#E80080', '#404040', '#9BC850'))

b_chart = pygal.Bar(style=custom_style)

b_chart.title = "First Twenty Wireshark searches"
b_chart.add("TLS", [9])
b_chart.add("TCP", [9])
b_chart.add("DNS", [2])
b_chart.render_in_browser()