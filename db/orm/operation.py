import sys
sys.path.append('.')
from models import UserInfo
from utils import Base, DBsession, eng


if __name__ == "__main__":
    Base.metadata.create_all(eng)
    info = [('10','xiaowang',100,10,2000),
            ('11','小明',1,0,0),
            ('12','mamamiya~ Boom',30,3,100)]
    fields = ('mid','name','fans','videonum','watch')
    user_list = (UserInfo(**dict(zip(fields,i))) for i in info)
    session = DBsession()
    session.add_all(user_list)
    session.commit()
    session.close()