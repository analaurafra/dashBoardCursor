## Dashboard de Vendas (PostgreSQL + Streamlit)

Aplicação interativa em Python para acompanhar vendas de uma concessionária (base existente em PostgreSQL).

### Como rodar

- **1) Crie o ambiente e instale dependências**

```powershell
cd dashBoardCursor
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

- **2) Configure a conexão com o Postgres**

Copie o arquivo de exemplo e ajuste os valores:

```powershell
copy config.example.toml config.toml
```

- **3) Inicie o dashboard**

Importante: o `app.py` fica dentro da pasta `dashBoardCursor`.

```powershell
cd dashBoardCursor
streamlit run app.py
```

Ou, a partir da pasta pai (`dashBoard_Cursor`):

```powershell
.\run.ps1
```

### Observações

- O arquivo `config.toml` fica ignorado no git (veja `.gitignore`).
- O dashboard usa as tabelas: `vendas`, `veiculos`, `concessionarias`, `cidades`, `estados`, `clientes`, `vendedores`.

