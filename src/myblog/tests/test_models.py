
import pytest
from sqlalchemy import Column, Integer, String, Text

from ..database import Base, db_session, engine


class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    content = Column(Text)

    def __repr__(self):
        return "<Post(id='{}', title='{}')>".format(self.id, self.title)


@pytest.fixture(scope="function")
def session():
    Base.metadata.create_all(engine)
    yield db_session
    Base.metadata.drop_all(bind=engine, tables=[Sample.__table__])

def test_commit(session):

    sample = Sample(title='123', content='asdf')
    session.add(sample)
    session.commit()
    result = Sample.query.all()
    assert len(result) == 1
    assert result[0] == sample


