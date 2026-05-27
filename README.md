# 📊 Dashboard de Vendas

Um dashboard interativo e responsivo para acompanhar vendas de uma concessionária, construído com **Python**, **Streamlit** e **PostgreSQL**.

## 🎯 Sobre o Projeto

Este dashboard oferece uma visão completa e em tempo real das operações de vendas de uma concessionária, permitindo análises detalhadas por:
- Vendedores e performance
- Veículos mais vendidos
- Cidades e estados
- Clientes e histórico
- Tendências de vendas

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Streamlit** - Framework para criar interfaces web interativas
- **PostgreSQL** - Banco de dados relacional
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:
- Python 3.8 ou superior
- PostgreSQL 12 ou superior
- Git
- PowerShell (para Windows)

## 🚀 Instalação e Configuração

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/analaurafra/dashBoardCursor.git
cd dashBoardCursor
```

### 2️⃣ Crie o Ambiente Virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure a Conexão com PostgreSQL

1. Copie o arquivo de exemplo:

```powershell
copy config.example.toml config.toml
```

2. Edite o arquivo `config.toml` com suas credenciais:

```toml
[database]
host = "localhost"
port = 5432
database = "seu_banco_dados"
user = "seu_usuario"
password = "sua_senha"
```

> ⚠️ **Importante:** O arquivo `config.toml` é ignorado no git por segurança (veja `.gitignore`).

### 5️⃣ Inicie o Dashboard

**Opção 1 - Usando PowerShell (Windows):**
```powershell
cd dashBoardCursor
.\run.ps1
```

**Opção 2 - Usando Streamlit diretamente:**
```powershell
cd dashBoardCursor
streamlit run app.py
```

O dashboard abrirá automaticamente em: `http://localhost:8501`

## 📁 Estrutura do Projeto

```
dashBoardCursor/
├── dashBoardCursor/
│   ├── app.py                 # Aplicação principal
│   ├── config.py              # Configurações e carregamento de variáveis
│   ├── requirements.txt        # Dependências do projeto
│   └── ...
├── config.example.toml        # Arquivo de exemplo de configuração
├── run.ps1                    # Script para iniciar a aplicação
├── README.md                  # Este arquivo
└── .gitignore                 # Arquivos ignorados pelo git
```

## 📊 Tabelas do Banco de Dados

O dashboard utiliza as seguintes tabelas PostgreSQL:

| Tabela | Descrição |
|--------|-----------|
| `vendas` | Registros de vendas realizadas |
| `veiculos` | Catálogo de veículos disponíveis |
| `vendedores` | Dados dos vendedores |
| `clientes` | Informações dos clientes |
| `concessionarias` | Dados das concessionárias |
| `cidades` | Localidades atendidas |
| `estados` | Estados/províncias |

## 🎬 Como Usar

1. **Inicie a aplicação** seguindo as instruções de instalação
2. **Navegue pelo dashboard** usando a barra lateral
3. **Filtre dados** conforme necessário
4. **Exporte relatórios** (quando disponível)

## 🖼️ Visualizações Disponíveis

- Gráficos de vendas por período
- Performance de vendedores
- Distribuição geográfica
- Análise de veículos mais vendidos
- Tendências e previsões
- KPIs principais

## ⚙️ Configurações Avançadas

### Variáveis de Ambiente

Você pode usar variáveis de ambiente em vez do `config.toml`:

```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=seu_banco
export DB_USER=seu_usuario
export DB_PASSWORD=sua_senha
```

### Personalização do Tema

Edite `.streamlit/config.toml` para customizar a aparência:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## 🐛 Troubleshooting

### Erro de Conexão com PostgreSQL
- Verifique se o PostgreSQL está rodando
- Confirme as credenciais em `config.toml`
- Teste a conexão: `psql -h localhost -U seu_usuario -d seu_banco`

### Dependências com Conflito
```bash
pip install --upgrade -r requirements.txt
```

### Porta 8501 Já em Uso
```bash
streamlit run app.py --server.port 8502
```

## 🎬 Captura de Tela (Screenshots e GIFs)

### Se o GIF não estiver exibindo:

**1. Verifique o caminho do arquivo:**
- O arquivo GIF deve estar em uma pasta `assets/` ou no diretório raiz
- Use um caminho relativo correto:

```markdown
![Demo do Dashboard](./assets/demo.gif)
```

**2. Use HTML para melhor compatibilidade:**

```html
<div align="center">
  <img src="./assets/demo.gif" alt="Dashboard Demo" width="80%" />
</div>
```

**3. Converta GIF para WebP (mais leve):**

```bash
ffmpeg -i demo.gif -c vp9 demo.webp
```

Depois adicione ao README:

```html
<img src="./assets/demo.webp" alt="Demo do Dashboard" width="100%">
```

**4. Converta para vídeo MP4 (mais eficiente):**

```bash
ffmpeg -i demo.gif demo.mp4
```

Adicione o vídeo:

```html
<video width="100%" controls>
  <source src="./assets/demo.mp4" type="video/mp4">
  Seu navegador não suporta reprodução de vídeo.
</video>
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor

**Ana Laura França**  
- GitHub: [@analaurafra](https://github.com/analaurafra)

## 📞 Suporte

Encontrou um problema? Abra uma [issue](https://github.com/analaurafra/dashBoardCursor/issues) no GitHub.

---

**Última atualização:** Maio 2026  
**Versão:** 1.0.0
