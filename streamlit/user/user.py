from sessionstate import _get_full_session

class User():
    def __init__(self):
        self.current_username = _get_active_user()

    def check_user_exists(self):
        return True

def _get_active_user():
    session = _get_full_session()
    user = session.ws.request.headers['X-Forwarded-User']
    return user