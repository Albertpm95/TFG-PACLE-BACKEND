from sqlalchemy import create_engine, MetaData

engine = create_engine("jdbc:postgresql://localhost:5432/pacle")

conn = engine.connect()
meta_data = MetaData()
