import random
import datetime
from faker import Faker
from app import db, Venda

fake = Faker("pt_BR")

# Lista de produtos fictícios
produtos = ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Fone Bluetooth", 
            "Teclado Mecânico", "Mouse Gamer", "Monitor 27'", "SSD 1TB", "Cadeira Gamer"]

# Criando 500 vendas fictícias
def gerar_dados():
    vendas = []
    for _ in range(500):
        data_venda = fake.date_between(start_date="-6M", end_date="today")  # Últimos 6 meses
        produto = random.choice(produtos)
        quantidade = random.randint(1, 5)  # Quantidade entre 1 e 5 unidades
        cliente_id = random.randint(1000, 9999)  # IDs fictícios para clientes
        promocao = random.choice([True, False])  # Produto estava ou não em promoção

        venda = Venda(
            data_venda=data_venda,
            produto=produto,
            quantidade=quantidade,
            cliente_id=cliente_id,
            promocao=promocao
        )
        vendas.append(venda)

    return vendas

# Inserindo no banco
def popular_banco():
    with db.session.begin():
        vendas = gerar_dados()
        db.session.add_all(vendas)
        db.session.commit()
        print(f"📌 {len(vendas)} registros inseridos com sucesso!")

if __name__ == "__main__":
    with db.app.app_context():
        popular_banco()