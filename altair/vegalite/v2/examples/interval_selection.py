"""
Interval Selection Example
==========================

This is an example of creating a stacked chart for which the domain of the
top chart can be selected by interacting with the bottom chart.
"""
# category: area charts

import altair as alt
from vega_datasets import data
sp500 = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

upper = alt.Chart().mark_area().encode(
    alt.X('date:T', scale={'domain': brush.ref()}),
    y='price:Q'
).properties(
    width=600,
    height=200
)

lower = upper.properties(
    selection=brush,
    height=60
)

alt.vconcat(upper, lower, data=sp500)
