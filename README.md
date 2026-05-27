# 📊 Sales Dashboard

An interactive and responsive dashboard to track sales of a car dealership, built with **Python**, **Streamlit**, and **PostgreSQL**.

## 🎯 About the Project

This dashboard provides a comprehensive and real-time view of a car dealership's sales operations, enabling detailed analysis by:
- Sales representatives and performance
- Best-selling vehicles
- Cities and states
- Customers and history
- Sales trends

## 🛠️ Technologies Used

- **Python 3.8+** - Primary language
- **Streamlit** - Framework for creating interactive web interfaces
- **PostgreSQL** - Relational database
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations

## 📋 Prerequisites

Before starting, make sure you have installed:
- Python 3.8 or higher
- PostgreSQL 12 or higher
- Git
- PowerShell (for Windows)

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/analaurafra/dashBoardCursor.git
cd dashBoardCursor
```

### 2️⃣ Create Virtual Environment

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

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL Connection

1. Copy the example file:

```powershell
copy config.example.toml config.toml
```

2. Edit the `config.toml` file with your credentials:

```toml
[database]
host = "localhost"
port = 5432
database = "your_database_name"
user = "your_username"
password = "your_password"
```

> ⚠️ **Important:** The `config.toml` file is ignored in git for security reasons (see `.gitignore`).

### 5️⃣ Start the Dashboard

**Option 1 - Using PowerShell (Windows):**
```powershell
cd dashBoardCursor
.\run.ps1
```

**Option 2 - Using Streamlit directly:**
```powershell
cd dashBoardCursor
streamlit run app.py
```

The dashboard will automatically open at: `http://localhost:8501`

## 📁 Project Structure

```
dashBoardCursor/
├── dashBoardCursor/
│   ├── app.py                 # Main application
│   ├── config.py              # Configuration and variable loading
│   ├── requirements.txt        # Project dependencies
│   └── ...
├── config.example.toml        # Example configuration file
├── run.ps1                    # Script to start the application
├── README.md                  # This file
└── .gitignore                 # Files ignored by git
```

## 📊 Database Tables

The dashboard uses the following PostgreSQL tables:

| Table | Description |
|--------|-----------|
| `vendas` | Sales records |
| `veiculos` | Available vehicles catalog |
| `vendedores` | Sales representatives data |
| `clientes` | Customer information |
| `concessionarias` | Dealership data |
| `cidades` | Cities served |
| `estados` | States/provinces |

## 🎬 How to Use

1. **Start the application** following the installation instructions
2. **Navigate through the dashboard** using the sidebar
3. **Filter data** as needed
4. **Export reports** (when available)

## 🖼️ Available Visualizations

- Sales charts by period
- Sales representative performance
- Geographic distribution
- Best-selling vehicles analysis
- Trends and forecasts
- Key performance indicators (KPIs)

## ⚙️ Advanced Configuration

### Environment Variables

You can use environment variables instead of `config.toml`:

```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=your_database
export DB_USER=your_username
export DB_PASSWORD=your_password
```

### Theme Customization

Edit `.streamlit/config.toml` to customize the appearance:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## 🐛 Troubleshooting

### PostgreSQL Connection Error
- Verify that PostgreSQL is running
- Confirm credentials in `config.toml`
- Test the connection: `psql -h localhost -U your_username -d your_database`

### Conflicting Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Port 8501 Already in Use
```bash
streamlit run app.py --server.port 8502
```

## 🎬 Screenshots and GIFs

### If the GIF is not displaying:

**1. Check the file path:**
- The GIF file should be in an `assets/` folder or in the root directory
- Use a correct relative path:

```markdown
![Dashboard Demo](./assets/demo.gif)
```

**2. Use HTML for better compatibility:**

```html
<div align="center">
  <img src="./assets/demo.gif" alt="Dashboard Demo" width="80%" />
</div>
```

**3. Convert GIF to WebP (lighter file):**

```bash
ffmpeg -i demo.gif -c vp9 demo.webp
```

Then add to README:

```html
<img src="./assets/demo.webp" alt="Dashboard Demo" width="100%">
```

**4. Convert to MP4 video (more efficient):**

```bash
ffmpeg -i demo.gif demo.mp4
```

Add the video:

```html
<video width="100%" controls>
  <source src="./assets/demo.mp4" type="video/mp4">
  Your browser does not support video playback.
</video>
```

## 🤝 Contributing

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is under the MIT License. See the LICENSE file for more details.

## 👤 Author

**Ana Laura França**  
- GitHub: [@analaurafra](https://github.com/analaurafra)

## 📞 Support

Found an issue? Open an [issue](https://github.com/analaurafra/dashBoardCursor/issues) on GitHub.

---

**Last updated:** May 2026  
**Version:** 1.0.0
