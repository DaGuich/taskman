from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates, relationship

Base = declarative_base()


class OrmMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Task(OrmMixin, Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)

    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project', back_populates='tasks')

    @validates('priority')
    def validate_priority(self, key, prio):
        assert(0 <= prio <= 10)
        return prio


class Project(OrmMixin, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    short = Column(String)

    tasks = relationship('Task', order_by=Task.id, back_populates='project')
