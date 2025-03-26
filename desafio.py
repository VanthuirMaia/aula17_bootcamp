from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # Estabelece a relação entre Fornecedores e Produtos
    fornecedor = relationship("Fornecedor")

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo Fornecedores
try:
    with Session() as session: #Usando a sessão corretamente com o gerenciador de contexto
        fornecedores = [
            Fornecedor(nome="Forncedor A", telefone="12345678", email="contato@a.com", endereco="Rua A"),
            Fornecedor(nome="Forncedor B", telefone="78945612", email="contato@b.com", endereco="Rua B"),
            Fornecedor(nome="Forncedor C", telefone="65498765", email="contato@c.com", endereco="Rua C"),
            Fornecedor(nome="Forncedor D", telefone="32165498", email="contato@d.com", endereco="Rua D"),
            Fornecedor(nome="Forncedor E", telefone="12457896", email="contato@e.com", endereco="Rua E"),
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e: # Capturando exeções do SQLAlchemy
    print(f"Erro ao inserir fornecedores: {e}")

# Inserindo produtos
try:
    with Session() as session: # Corrigindo a utilização da sessão
        produtos = [
            Produto(nome="Produto 1", descricao="Descrição do P1", preco=100, fornecedor_id=1),
            Produto(nome="Produto 2", descricao="Descrição do P2", preco=200, fornecedor_id=2),
            Produto(nome="Produto 3", descricao="Descrição do P3", preco=300, fornecedor_id=3),
            Produto(nome="Produto 4", descricao="Descrição do P4", preco=400, fornecedor_id=4),
            Produto(nome="Produto 5", descricao="Descrição do P5", preco=500, fornecedor_id=5)
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e: # Capturando exeções do SQLAlchemy
    print(f"Erro ao inserir produtos: {e}")

from sqlalchemy import func