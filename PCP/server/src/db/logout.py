try:
    from src.utilities.swen_344_db_utils import exec_commit
except:
    from utilities.swen_344_db_utils import exec_commit


def user_logout(kwargs):
    session_key = kwargs.get('session_key')
    logout_query = '''UPDATE user_authentication SET session_key = NULL WHERE session_key = %s;'''
    exec_commit(logout_query, (session_key,))
    return {"message":"User Logout Successfully!"},200
