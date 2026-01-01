PYTHON_PATH="/usr/bin/python3"
VENV_DIR="django_venv"

$PYTHON_PATH -m venv $VENE_DIR
source $VENV_DIR/bin/activate

python3 -m pip install -r requirement.txt

python3 manage.py runserver