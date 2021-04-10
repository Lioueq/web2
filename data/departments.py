from sqlalchemy import orm
import sqlalchemy

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    def __repr__(self):
        return f'{self.id}|{self.title}|{self.chief}|{self.members}|{self.email}'
    __tablename__ = 'department'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    user = orm.relation('User')
