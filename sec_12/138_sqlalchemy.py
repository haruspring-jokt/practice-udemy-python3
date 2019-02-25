import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

# connect mysql
url = 'mysql+pymysql://root:root@localhost/test_mysql_database2?charset=utf8'
engine = sqlalchemy.create_engine(url, echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person_1 = Person(name='Mike')
session.add(person_1)
person_2 = Person(name='Nancy')
session.add(person_2)
person_3 = Person(name='Jun')
session.add(person_3)

session.commit()

person_4 = session.query(Person).filter_by(name='Mike').first()
person_4.name = 'Michel'
session.commit()

person_5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(person_5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
