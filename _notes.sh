# connect using:
# ssh azure@ip.ip.ip.ip

sudo su
apt-get update -y 
apt-get install -y python python-pip
pip install flask

# COPY app.py /opt/
FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=80

docker run -d -p 8080:8080 fabenavideso/simple-app

