# Python Virtual Environment Setup

This project uses a Python virtual environment to manage dependencies. Follow the steps below to set up the environment and install the required packages.

---

## 🐍 Create a Virtual Environment

### Execute install_deps script

```bash
# Give execution permissions
chmod +x ./install_deps.sh ;

# Run it
./install_deps.sh;
```

### Activate venv and run script

```bash
source venv/bin/activate ;
python3 main.py ;

# To check if venv is activate or not, this command should have an output
echo $VIRTUAL_ENV;
```

### Deactivate venv
```bash
deactivate
```

