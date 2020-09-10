import os

from sqlalchemy import (Column, MetaData, String, Integer, Table, create_engine)
from sqlalchemy.sql import func
from databases import Database

# get database url from the environment
DB_URL = os.getenv("DB_URL")

#SQLAlchemy
#create database engine
engine = create_engine(DB_URL)

#init metadata store
metadata = MetaData()

#create table
#i.e. CREATE TABLE users(Id varcahr(10) PRIMARY_KEY, Name varchar(50))
users = Table(
    "users",
    metadata,
    Column("Id", Integer, primary_key=True),
    Column("Name", String(50)),
)

# init databases query builder
database = Database(DB_URL)
