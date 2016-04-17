#!/bin/bash
# Build Environment
virtualenv env
source env/bin/activate

# Install Requirements
echo "[x] Installing requirements..."
pip install -r requirements.txt

# Done
echo "[.] Done"

# Help
echo ""
echo "Queries can be submitted to the script: python main.py [statement]"
