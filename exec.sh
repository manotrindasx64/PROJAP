#!/bin/bash

cd "$(dirname "$0")"

# Ativa o ambiente
source /home/adriellucas/PROJS_DEV/PROJAP/.venv/bin/activate

# Configurações de ambiente
export QT_QPA_PLATFORM=offscreen
export QT_LOGGING_RULES='*.debug=false;qt.qpa.*=false'
export PYTHONWARNINGS="ignore"


# Roda o Python
python3 /home/adriellucas/PROJS_DEV/PROJAP/main.py

