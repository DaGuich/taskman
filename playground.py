from taskman import dbif
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    dbif.Base.metadata.create_all(engine)

    samproject = dbif.Project(name='Default', short='def')
    session.add(samproject)

    proj = session.query(dbif.Project).filter_by(name='Default').first()
    print(samproject is proj)

    session.commit()
