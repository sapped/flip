from sessionstate import _get_full_session

def get_user():
    session = _get_full_session()
    user = session.ws.request.headers['X-Forwarded-User']
    return user