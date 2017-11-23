from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

DSNs = {
    'mysql':'mysql+pymysql://'
}