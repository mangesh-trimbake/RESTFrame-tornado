##SQLAlchmey Integration

# SQLAlchmey Basics
```
#approch 1st

engine = create_engine("msql_url")

session = Session(engine)

Base = declarative_base()

Base.metadata.create_all(engine) # this create the table changes

session.query(model_name).all() # select query

```

# SQLAlchmey scoped session with query_property
```
#approch 2nd

engine = create_engine("msql_url")

session = scoped_session(sessionmaker(engine))

model_class.query = session.query_property()
Base = declarative_base(cls=model_class)

 
Base.metadata.create_all(engine) # this create the table changes
Base.metadat.bind = engine

session.query(model_name).all() # select query 1st approch
model_name.all() # select query 2nd approch

```

# RESTFrame-tornado
stacks for development with micro Web framework to create REST API with help of Tornado Python, SQLAlchemy, sqlacodegen.
## How to scaffold controller/handeler classes using RESTFrame
```
cd RESTFrame
python restframe.py rest table_name
```
