from main import User
from main import db
from faker import Faker

f=Faker()

def create_users(n=10):
    n=int(n)
    for i in range(n):
        u=User(username=f.unique.user_name())
        db.session.add(u)
    db.session.commit()

def delete_user(name):
    db.session.delete(name)
    db.session.commit()

if __name__ == '__main__':
    #print('Hello')
    #User.query.delete()
    for u in User.query.all():
        db.session.delete(u)
    db.session.commit()
    create_users(500)
