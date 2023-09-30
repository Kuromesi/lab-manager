from service.session import session
from table.lab_user import User
from utils.logger import logger

def add_user(user_name):
    user = session.query(User).filter(User.name == user_name).all()
    if len(user) > 0:
        logger.warning(f"user {user_name} already exist")
    else:
        user = User(name=user_name)
        session.add(user)
        session.commit()
        logger.info(f"add user {user_name} success")

def del_user(user_name):
    user = session.query(User).filter(User.name == user_name).all()
    if len(user) == 0:
        print(f"user {user_name} not found")
    else:
        logger.info(f"deleting user {user_name}")
        if len(user) > 1:
            logger.warning(f"multiple user {user_name} found")
            for u in user:
                session.delete(u)
        else:
            session.delete(user[0])
        session.commit()