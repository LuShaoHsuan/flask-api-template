from sqlalchemy import text
from sqlalchemy.dialects.postgresql import JSONB, INTEGER, VARCHAR, TIMESTAMP, NUMERIC

from . import db


class TableObject(db.Model):
    __tablename__ = ''
    column = db.Column()

    @property
    def serialize(self):
        return {'': self.column}

    def add_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()
