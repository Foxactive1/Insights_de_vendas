from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import plotly.express as px
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.Date, nullable=False)
    produto = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer, nullable=False)
    promocao = db.Column(db.Boolean, default=False)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/insights')
def insights():
    vendas = Venda.query.all()
    df = pd.DataFrame([(v.data_venda, v.produto, v.quantidade, v.promocao) for v in vendas],
                      columns=['data_venda', 'produto', 'quantidade', 'promocao'])
    
    # 📊 Produtos mais vendidos
    top_produtos = df.groupby('produto')['quantidade'].sum().nlargest(5).to_dict()

    # 📉 Produtos menos vendidos
    low_produtos = df.groupby('produto')['quantidade'].sum().nsmallest(5).to_dict()

    # 📈 Impacto de Promoções
    impacto_promocao = df.groupby('promocao')['quantidade'].sum().to_dict()

    # 📈 Previsão de Vendas (90 dias)
    df_tempo = df.groupby('data_venda')['quantidade'].sum().asfreq('D').fillna(0)
    modelo = ExponentialSmoothing(df_tempo, trend='add', seasonal='add', seasonal_periods=30).fit()
    previsao = modelo.forecast(90).to_dict()

    return jsonify({
        "top_produtos": top_produtos,
        "low_produtos": low_produtos,
        "impacto_promocao": impacto_promocao,
        "previsao_vendas": previsao
    })

@app.route('/grafico')
def grafico():
    vendas = Venda.query.all()
    df = pd.DataFrame([(v.data_venda, v.produto, v.quantidade) for v in vendas],
                      columns=['data_venda', 'produto', 'quantidade'])
    
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    df = df.groupby('data_venda').sum().reset_index()
    
    fig = px.line(df, x='data_venda', y='quantidade', title="Tendência de Vendas", markers=True)
    return fig.to_html(full_html=False)

if __name__ == '__main__':
    app.run(debug=True)