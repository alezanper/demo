# connect to ubuntu machine using:
# ssh azure@ip.ip.ip.ip

sudo su
apt-get update -y 
apt-get install -y python python-pip
pip install flask

# COPY app.py /opt/
FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=80