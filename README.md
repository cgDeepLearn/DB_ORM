# DB_ORM

# 一个python连接操作多种数据库的api包括使用ORM(sqlalchemy)
暂添加了sqlite、mysql和postgresql

# 使用：
1. git clone
2. 切换到工程主目录建立env和依赖
```python
virtualenv dbenv # 建立虚拟环境dbenv
source dbenv/bin/activate  # 激活python虚拟环境，windows下进入dbenv/bin目录
运行activate
# 如果你是用pyvenv或者conda env等都可以
pip install -r requirements.txt  # 安装依赖项
```
3. 进入config文件夹，修改配置文件db.fig
```python
# 各数据库参数可根据你本地安装环境配置，
# 例如只安装了postgresql，则只设置postgresql下各项配置，engine=1
[dbtype]
db0 = mysql
db1 = postgresql
db2 = sqlite

[mysql]
host = 127.0.0.1
dbname = testdb
user = test
password = test
port = 3306

[postgresql]
host = 127.0.0.1
dbname = testdb
user = test
password = test
port = 5432

[sqlite]
dbname = testdb
# engine
#使用sqlalchemy的engine
#默认为0(mysql),可根据你的本地数据库和虚拟环境使用不同的engine
# 0-mysql,1-postgresql,2-sqlite
[engine]
dbindex = 0
```

4. 配置logger文件夹下mylog.py下的logging模块需要读取的dictConfig
```python
log_dir = BASE_DIR + '/logs'  # log文件在主目录的logs文件下
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_path = os.path.join(log_dir, 'test.log')  # log文件名
```

5. 确保已经进入dbenv虚拟环境,未进入请运行：
```python
source activate dbenv/bin/activate # windwods请使用上面提到的相应方法
```
在主目录再运行简单的测试程序
```python
python tests/test_db.py  # 测试普通的数据库增删改查
python tests/orm.py  # 测试ORM
python tests/logger.py  # 测试logger模块
```