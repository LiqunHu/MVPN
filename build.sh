#!/bin/bash
docker build -t fox/py3gunicorn .
docker run --rm -p 127.0.0.1:3306:3306 --name testsql -v $PWD/mysql/logs:/logs -v $PWD/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql

sleep 10

docker run --rm -it --link testsql:testsql -v $PWD/sql:/sql  mysql bash -c "mysql -htestsql -uroot -p123456</sql/sequence.sql"

docker run --rm -it --link testsql:testsql -v $PWD/servdata/logs:/logs -v $PWD:/webapp -w /webapp fox/py3gunicorn python CreateTables.py

docker run -d --rm --name testserver --link testsql:testsql -v $PWD/servdata/logs:/logs -v $PWD/static:/webfiles -v $PWD:/webapp -w /webapp fox/py3gunicorn gunicorn -b 0.0.0.0:9000 MainServer:app

docker run --rm -v $PWD/frontEnd/:/webapp -w /webapp node npm install

cd ./static/static/dependencies

bash link.sh

cd -

docker run --rm --name testweb -v $PWD/frontEnd/:/webapp -w /webapp -d node npm run dev

docker run --rm -p 80:80 --name putnginx --link testserver:testserver --link testweb:testweb -v $PWD/nginxConf:/etc/nginx/conf.d/ -v $PWD/static:/static -d nginx
