from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    """Data model."""
    __tablename__ = "tProjects"
    __table_args__ = {"schema":"dbo"}

    ProjectID = Column(Integer, primary_key=True, nullable=False)
    ProjectName = Column(Text, nullable=False)
    ProjectDescription = Column(Text, nullable=True)
    UserID = Column(Integer, nullable=False)
    CreatedBy = Column(Integer, nullable=False)
    CreatedOn = Column(DateTime, nullable=False)
    ModifiedBy = Column(Integer, nullable=False)
    ModifiedOn = Column(Integer, nullable=False)
    IsActive =  Column(Boolean, nullable=False)
    
    def __repr__(self):
        return '<Project model {}>'.format(self.id)
