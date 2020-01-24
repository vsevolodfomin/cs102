import datetime as dt
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей
    Возраст считается как медиана среди возраста всех друзей пользователя
    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    friends = get_friends(user_id, "bdate")
    friends = [User(**friend) for friend in friends]
    ages = []

    for friend in friends:
        if friend.bdate is not None:
            data = friend.bdate.split(".")
            if len(data) == 3:
                age = dt.datetime.now().year - int(data[2])
                born_month = int(data[1])
                born_day = int(data[0])
                if (dt.datetime.now().month < born_month) or (
                        dt.datetime.now().month == born_month and dt.datetime.now().day < born_day):
                    ages.append(age - 1)
                else:
                    ages.append(age)
    if len(ages) > 0:
        return median(ages)
    else:
        return None
