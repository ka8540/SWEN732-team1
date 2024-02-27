import pandas as pd
try:
    from model.User import User
    from utilities.swen_344_db_utils import *
except ImportError:
    from src.model.User import User
    from src.utilities.swen_344_db_utils import *

class UserRepository:
    table = "users"
    def create(user: User):
        json_data = {}
        for key, value in user.__dict__.items():
            if value is None:
                continue
            json_data[key.replace("_User__", "")] = value
        df = pd.DataFrame.from_dict([json_data])
        return commit_dataframe(df, UserRepository.table)

    def update(user: User):
        json_data = {}
        for key, value in user.__dict__.items():
            if value is None:
                continue
            json_data[key.replace("_User__", "")] = value
        id = json_data.pop("id")
        df = pd.DataFrame.from_dict([json_data])
        update_dataframe(df, UserRepository.table, id)

    def get_by_id(id) :
        query = """
        SELECT id, first_name, last_name, email, phone_number, username, password_hash, session_key 
        FROM users 
        WHERE id=%s;
        """
        values = (id,)
        result = exec_get_one(query, values)
        if result is not None:
            return User(
                id=result[0],
                first_name= result[1],
                last_name=result[2],
                email=result[3],
                phone_number= result[4],
                username= result[5],
                password_hash= result[6],
                session_key= result[7]
            )
        return None

    def get_all():
        query = """
        SELECT id, first_name, last_name, email, phone_number, username, password_hash, session_key 
        FROM users 
        """
        values = (id,)
        results = exec_get_all(query, values)
        if results is not None:
            return [User(
                id=result[0],
                first_name= result[1],
                last_name=result[2],
                email=result[3],
                phone_number= result[4],
                username= result[5],
                password_hash= result[6],
                session_key= result[7]
            ) for result in results]
        return None

    def delete(user: User):
        query = """
        DELETE 
        FROM users 
        WHERE id=%s;
        """
        values = (user.id,)
        result = exec_commit(query, values)
        return result
