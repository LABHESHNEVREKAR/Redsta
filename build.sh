pip install --upgrade pip
pip install -r requirements.txt

#!/usr/bin/env bash
echo "Installing Python 3.11..."
apt-get update
apt-get install -y python3.11 python3.11-venv python3.11-dev
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
python3 --version
