from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    """Data model."""
    __tablename__ = "tProjectKeys2"
    __table_args__ = {"schema":"KnowHow.dbo"}

    id = Column(Integer, primary_key=True, nullable=False)
    webKey = Column(Text, nullable=False)
    mobileKey = Column(Text, nullable=True)
    '''
    UserID = Column(Integer, nullable=False)
    CreatedBy = Column(Integer, nullable=False)
    CreatedOn = Column(DateTime, nullable=False)
    ModifiedBy = Column(Integer, nullable=False)
    ModifiedOn = Column(Integer, nullable=False)
    IsActive =  Column(Boolean, nullable=False)
    '''
    
    def __repr__(self):
        return '<Project model {}>'.format(self.id)
