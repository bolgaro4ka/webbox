import os
import argparse
parser = argparse.ArgumentParser(
                    prog='Script for run server',
                    description='Run server',
                    epilog='Enjoy the script!')

parser.add_argument('what')
args = parser.parse_args()
if 'i' in args.what: 
    os.system('python -m venv venv')
    os.system('venv\\Scripts\\activate')
    os.system('pip install -r req.txt')
os.system('.\\venv\\Scripts\\activate')
os.system('cd webbox')
if 'm' in args.what: 
    os.system('python webbox/manage.py makemigrations')
    os.system('python webbox/manage.py migrate')
if 's' in args.what: os.system('python webbox/manage.py runserver 10.167.30.11:8000')
if 'e' in args.what: os.system('python webbox/manage.py runserver 127.0.0.1:8000')