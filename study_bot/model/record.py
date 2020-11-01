from study_bot.lib import custom_except
from dateutil.parser import parse
from datetime import datetime, timedelta, timezone

COL = None


def setup(db):
    global COL
    COL = db["record"]


def add(data):
    """
        data = {
            "userId": "higheighaie",
            "date": "2019/10/01",
            "type": "uva",
            "number": "123",
        }
    """
    filter_ = {
        "userId": data["userId"],
        "type": data["type"],
        "number": data["number"],
    }
    if COL.find_one(filter_) is None:
        COL.insert_one(
            {
                "userId": data["userId"],
                "date": parse(data["date"]),
                "type": data["type"],
                "number": data["number"],
            }
        )
    else:
        raise custom_except.duplicateError


def get_recent(user_id):
    # interval = 30
    interval = 30
    end_date = datetime.now(tz=timezone.utc)
    start_date = end_date.replace(
        hour=0, minute=0, second=0, microsecond=0
    ) - timedelta(days=30)
    filter_ = {
        "userId": user_id,
        "date": {"$gte": start_date, "$lte": end_date},
    }
    proj = {"_id": 0, "date": 1}
    return list(COL.find(filter_, proj))
