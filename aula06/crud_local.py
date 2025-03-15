from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# Constantes
HOST = 'localhost'
USER = 'root'
PASSWORD = 'ceub123456'
DB = 'db_central_servicos'

engine = create_engine(f'mysql://{USER}:{PASSWORD}@{HOST}:3306/{DB}?charset=utf8')

# Auto mapeando as tabelas tb_local
base = automap_base()
base.prepare(autoload_with=engine)
tb_local = base.classes.tb_local

# Implementando CRUD de tb_local
def listar_locais():
    with Session(engine) as session:
        locais = session.query(tb_local).all()
        print("\nLista de Locais:")
        for local in locais:
            print(
                f"""
                    Nome: {local.nme_local} 
                    Latitude: {local.lat_local}
                    Longitude: {local.lgt_local}
                    Status: {local.sts_local}
                """)

def consultar_local():
    nome = input("Digite o nome do local a consultar: ")
    with Session(engine) as session:
        local = session.query(tb_local).filter(tb_local.nme_local == nome).first()
        if local:
            print(
                f"""
                    Nome: {local.nme_local} 
                    Latitude: {local.lat_local}
                    Longitude: {local.lgt_local}
                    Status: {local.sts_local}
                """)
        else:
            print("Local não encontrado.")

def incluir_local():
    nme_local = input("Digite o nome do local: ")
    lat = float(input("Digite a latitude do local: "))
    long = float(input("Digite a longitude do local: "))
    with Session(engine) as session:
        novo_local = tb_local()
        novo_local.nme_local = nme_local
        novo_local.lat_local = lat
        novo_local.lgt_local = long
        novo_local.sts_local = 'A'
        session.add(novo_local)
        session.commit()
        print("Local incluído com sucesso! ID: ", novo_local.idt_local)

def alterar_local():
    nme = input("Digite o nome do local a alterar: ")
    with Session(engine) as session:
        local = session.query(tb_local).filter(tb_local.nme_local == nme).first()
        if local:
            print(
                f"Local: {local.nme_local}, Latitude: {local.lat_local}, Longitude: {local.lgt_local}, Status: {local.sts_local}")
            local.nme_local = input("Digite o novo nome do local: ")
            local.lat_local = float(input("Digite a nova latitude do local: "))
            local.lgt_local = float(input("Digite a nova longitude do local: "))
            local.sts_local = input("Digite o novo status do local: ")
            session.commit()
            print("Local alterado com sucesso!")
        else:
            print("Local não encontrado.")

def excluir_local():
    nme = input("Digite o nome do local a excluir: ")
    with Session(engine) as session:
        local = session.query(tb_local).filter(tb_local.nme_local == nme).first()
        if local:
            print(
                f"""
                    Nome: {local.nme_local} 
                    Latitude: {local.lat_local}
                    Longitude: {local.lgt_local}
                    Status: {local.sts_local}
                """)
            session.delete(local)
            session.commit()
            print("Local excluído com sucesso!")
        else:
            print("Local não encontrado.")

def menu():
    while True:
        print("\n--- Menu locais ---")
        print("1. Listar locais")
        print("2. Consultar local")
        print("3. Incluir local")
        print("4. Alterar local")
        print("5. Excluir local")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_locais()
        elif opcao == '2':
            consultar_local()
        elif opcao == '3':
            incluir_local()
        elif opcao == '4':
            alterar_local()
        elif opcao == '5':
            excluir_local()
        elif opcao == '0':
            engine.dispose()
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
