from collections import Counter
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
"""
import chart_studio.plotly as py
import plotly.graph_objs as go
"""
from typing import List, Tuple

from api import messages_get_history
from api_models import Message
import config


Dates = List[datetime.date]
Frequencies = List[int]


plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: List[Message]) -> Tuple[Dates, Frequencies]:
    """ Получить список дат и их частот
    :param messages: список сообщений
    """
    messages = messages_get_history(id, offset=offset, count=count)
    for message in messages:
        date = fromtimestamp(message.date)
        try:
            Frequencies[Dates.index(date)] += 1
        except:
            Dates.append(date)
            Frequencies.append(1)

    Dates.reverse()
    Frequencies.reverse()
    message_count = (Dates, Frequencies)
    return message_coun


def plotly_messages_freq(dates: Dates, freq: Frequencies) -> None:
    """ Построение графика с помощью Plot.ly
    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    x = dates
    y = freq
    data = [go.Scatter(x=x, y=y)]
    py.iplot(data)


i = count_dates_from_messages(2947380, 0, 1500)
plotly_messages_freq(i[0], i[1])