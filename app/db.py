from databases import Database
import sqlalchemy
from sqlalchemy import MetaData, Column, DateTime, Integer, String, Table, ARRAY, JSON
from sqlalchemy.sql import func

DATABASE_URL = "postgresql://postgres:postgres@172.17.0.2/postgres"

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)

db_users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100), unique=True),
    Column("password", String(300)),
    Column("name", String(300)),
    Column("role", ARRAY(String)),
    Column("status", String(300)),
    Column("info", JSON),
    Column("created_date", DateTime, default=func.now(), nullable=False)
)