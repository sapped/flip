from sessionstate import _get_session

def get_user():
    session = _get_session()
    user = session.ws.request.headers['X-Forwarded-User']
    return user