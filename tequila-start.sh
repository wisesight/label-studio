echo "PROJECT_NAME=$1" > .env
echo "USER_EMAIL=$2" >> .env
echo "USER_PASSWORD=$3" >> .env
echo "USER_TOKEN=$4" >> .env
echo "NGINX_PORT=$5" >> .env
echo "COMPOSE_PROJECT_NAME=$6" >> .env
export PROJECT_NAME=$1
export USER_TOKEN=$4
export NGINX_PORT=$5
export COMPOSE_PROJECT_NAME=$6

# docker compose -f docker-compose.tequila.yaml up --build --force-recreate
docker compose -f docker-compose.tequila.yaml up -d --build --force-recreate
sleep 30 # waiting for label-studio services starting completely

if [ "$(docker ps -q -f name=${COMPOSE_PROJECT_NAME}-nginx-1)" ]\
&& [ "$(docker ps -q -f name=${COMPOSE_PROJECT_NAME}-app-1)" ] \
&& [ "$(docker ps -q -f name=${COMPOSE_PROJECT_NAME}-db-1)" ]; then
  echo "All label-studio services have been started..."
  python3 tequila-logo-setup.py --port ${NGINX_PORT} --token ${USER_TOKEN}
fi