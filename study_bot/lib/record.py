from datetime import datetime, timedelta, timezone
from collections import defaultdict


def gen_seq(records):
    # cnt
    cnt = defaultdict(lambda: 0)
    for cur_record in records:
        cnt[cur_record["date"].date()] += 1
    # start gen seq
    cur_date = datetime.now(tz=timezone.utc).date()
    result = {"labels": [], "data": []}
    for i in range(29, -1, -1):
        tmp_date = cur_date - timedelta(days=i)
        result["data"].append(cnt[tmp_date])
        result["labels"].append(tmp_date.strftime("%m/%d"))
    return result
