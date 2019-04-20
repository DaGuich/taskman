from taskman import dbif
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    dbif.Base.metadata.create_all(engine)

    user = dbif.User(username='GilchM', password='test', email_address='matthias@gilch.de')

    samproject = dbif.Project(name='Default', short='def')
    session.add(samproject)
    session.commit()

    additional = {'project': samproject, 'user': user}

    task = dbif.Task(title='First Task', description='Test', **additional)
    session.add(task)
    session.commit()
    task = dbif.Task(title='Second Task', description='Test', **additional)
    session.add(task)
    session.commit()
    task = dbif.Task(title='Third Task', description='Test', **additional)
    session.add(task)
    session.commit()

    proj = session.query(dbif.Project).filter_by(name='Default').first()
    print('\n'.join([x.title for x in proj.tasks]))
