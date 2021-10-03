#SQLAlchmey Integration

## SQLAlchmey Basics
```
#approch 1st

engine = create_engine("msql_url")

session = Session(engine)

Base = declarative_base()

Base.metadata.create_all(engine) # this create the table changes

session.query(model_name).all() # select query

```

# RESTFrame-tornado
stacks for development with micro Web framework to create REST API with help of Tornado Python, SQLAlchemy, sqlacodegen.
## How to scaffold controller/handeler classes using RESTFrame
```
cd RESTFrame
python restframe.py rest table_name
```
