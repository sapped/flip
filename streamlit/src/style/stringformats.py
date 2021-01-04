import datetime as dt

def es_date_format(x):
    return dt.datetime.fromtimestamp(x).strftime('%b %e, %Y %r')