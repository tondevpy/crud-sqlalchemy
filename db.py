from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base 
from hashlib import sha256

engine = create_engine('sqlite:///dados.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(100))
    senha = Column(String(100))

class Repositorio:

    def criar_usuario(nome, email, senha):

        senha_hash = sha256(senha.encode('utf-8')).hexdigest()
        cadastrar = Usuario(nome=nome, email=email, senha=senha_hash)
        with Session() as session:
            session.add(cadastrar)
            session.commit()

    def excluir_usuario(email):
        with Session() as session:
            # verifica se o email existe
            usuario = session.query(Usuario).filter_by(email=email).first()
            session.delete(usuario)
            session.commit()

    def editar_usuario(email, novo_nome, novo_email, nova_senha):
        with Session() as session:
            # verifica se o email existe
            usuario = session.query(Usuario).filter_by(email=email).first()
            
            senha_hash = sha256(nova_senha.encode('utf-8')).hexdigest()

            usuario.nome = novo_nome
            usuario.email = novo_email
            usuario.senha = senha_hash

            session.commit()
            print('Usuário atualizado com sucesso...')

        #lógica para editar dados do usuário 
    def localizar_usuario(email):
        try:
            with Session() as session:
                return session.query(Usuario).filter_by(email=email).first()
        except Exception as e:
            print(f'Ocorreu um erro ao localizar o usuário {e}' )
            return None

    def login_usuario(email, senha):
        with Session() as session:
            # verifica se o email existe
            usuario = session.query(Usuario).filter_by(email=email).first()

            if usuario and usuario.senha == senha:
                return usuario.email
            else:
                return False

Base.metadata.create_all(engine)