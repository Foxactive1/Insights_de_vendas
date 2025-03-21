📌 README.md

# 📊 Dashboard de Insights de Vendas  

Este projeto é um sistema de análise de vendas que fornece insights estratégicos a partir de um banco de dados **SQLite**. Ele inclui uma API desenvolvida em **Flask** e uma interface web interativa para visualizar gráficos e previsões de vendas.

---

## 🚀 **Recursos**
✔ Conexão com **SQLite** (adaptável para MySQL/PostgreSQL).  
✔ API em **Flask** para geração de insights.  
✔ Gráficos interativos usando **Plotly e Pandas**.  
✔ Previsão de vendas com **Holt-Winters**.  
✔ Interface simples e responsiva.

---

## 📦 **Instalação e Configuração**

### 1️⃣ **Clone este repositório**
```bash
git clone https://github.com/Foxactive1/InsightsVendas.git
cd InsightsVendas

2️⃣ Instale as dependências

pip install -r requirements.txt

3️⃣ Crie o banco de dados

python models.py

4️⃣ Execute o servidor Flask

python app.py

5️⃣ Acesse no navegador

http://127.0.0.1:5000/


---

📊 Endpoints da API

🔹 /insights

Retorna dados de vendas, incluindo:

Top 5 produtos mais vendidos

Top 5 produtos menos vendidos

Impacto das promoções

Previsão de vendas para 90 dias


🔹 /grafico

Retorna um gráfico da tendência de vendas.


---

📌 Tecnologias Utilizadas

Python 3.x

Flask

SQLite

Pandas

Plotly

Statsmodels



---

👨‍💻 Autor

Desenvolvido por Dione Castro Alves - LinkedIn

📌 InNovaIdeia Assessoria em Tecnologia ®

