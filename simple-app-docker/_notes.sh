docker ps

docker ps -a

docker build . -f Dockerfile -t simple-app

docker run -d -p 8080:8080 simple-app       # internal:external
