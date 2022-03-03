<<<<<<< HEAD
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey
from models import City
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Attribute for FileStorage"""
            cityList = []
            for obj in models.storage.all(City).values():
                if obj.state_id == self.id:
                    cityList.append(obj)
            return cityList
=======
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Attribute for FileStorage"""
            cityList = []
            for obj in models.storage.all(City).values():
                if obj.state_id == self.id:
                    cityList.append(obj)
            return cityList
>>>>>>> 1bc002ec0ecad7b93ea946ae73478b51c046d885
