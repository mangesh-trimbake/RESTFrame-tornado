from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session #, DeclarativeMeta
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.exc import SQLAlchemyError


class Model(object):
    #: Query class used by :attr:`query`. Defaults to
    # :class:`SQLAlchemy.Query`, which defaults to :class:`BaseQuery`.
    query_class = None

    #: Convenience property to query the database for instances of this model
    # using the current session. Equivalent to ``db.session.query(Model)``
    # unless :attr:`query_class` has been changed.
    query = None



class SQLAlchemy:
    def __init__(self,app = None):

        self.engine = None
        self.db_url = None
        self.metadata = None

        self.session = scoped_session(sessionmaker())

        self.model_class = Model

        # self.Model = self.make_declarative_base(self.model_class, self.metadata)
        model_class.query = self.session.query_property()
        self.Model = declarative_base(cls=model_class))

        


        if app is not None:
            self.init_app(app)
    
    # @classmethod
    def init_app(self, app):
        if app is not None:
            print("Intializing DB for app")
            self.db_url = app['config']['db_url']
            self.engine = create_engine(self.db_url, pool_recycle=3600)

            self.Model.metadata.bind = self.engine
            self.session.configure(bind=self.engine)



    def make_declarative_base(self,model,metadata=None):

        model.query = self.session.query_property()

        return declarative_base(cls=model)


