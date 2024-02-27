import datetime

def userParser(user_list):
    return {
        "id": user_list[0],
        "first_name": user_list[1],
        "last_name": user_list[2],
        "email": user_list[3],
        "phone_number": user_list[4],
        "username": user_list[5],
    }
