from service.lab_user import add_user, del_user

def test_add_user():
    add_user("kuromesi")

def test_del_user():
    del_user("kuromesi")

if __name__ == "__main__":
    test_add_user()