from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo=True, pool_size=10)

print("Conexão com SQLite estabelecida.")