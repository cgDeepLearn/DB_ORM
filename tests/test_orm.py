# -*- coding: utf8 -*-
"""
test orm
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.orm import UserInfo, UserInfoOperation, create_all


create_all()
info = [('13', '小红', 100, 10, 2000),
        ('14', '小花', 1, 0, 0),
        ('15', 'Mike', 30, 3, 100)]
fields = ('mid', 'name', 'fans', 'videonum', 'watch')
new_user = (UserInfo(**dict(zip(fields, info[0]))))
user_list = (UserInfo(**dict(zip(fields, i))) for i in info)  # generator
UserInfoOperation.add(new_user)
UserInfoOperation.add_all(user_list)
select_sql = "select * from userinfo where name='小花';"
print(UserInfoOperation.query_from_sql(select_sql))



