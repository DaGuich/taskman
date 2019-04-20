from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType, PasswordType
from sqlalchemy_utils import Timestamp
from sqlalchemy.orm import validates, relationship

Base = declarative_base()


class StdMixin(Timestamp):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class Task(StdMixin, Base):
    title = Column(String, nullable=False)
    description = Column(String)
    priority = Column(Integer, nullable=False, default=5)

    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    project = relationship('Project', back_populates='tasks')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='tasks')

    @validates('priority')
    def validate_priority(self, key, prio):
        assert(0 <= prio <= 10)
        return prio


class Project(StdMixin, Base):
    name = Column(String, nullable=False)
    short = Column(String, nullable=False, unique=True)

    tasks = relationship('Task', order_by=Task.id, back_populates='project')


class User(StdMixin, Base):
    username = Column(String, nullable=False, unique=True)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)
    first_name = Column(String)
    family_name = Column(String)
    email_address = Column(EmailType, nullable=False)

    tasks = relationship('Task', order_by=Task.id, back_populates='user')
