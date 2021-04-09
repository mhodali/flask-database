# flask-database
in this repo i use kubernetes to deploy flask api with mysql database 
## docker part
1. install docker 
2. install mysql 
3. build docker file:  `Docker build . -t flask-api`
## kubernetes part
1. Encode your password in your terminal: echo -n password | base64
2. Add the output to the flakapi-secrets.yml file at the db_root_password field
3. kubectl apply -f flaskapi-secrets.yml
4. kubectl apply -f mysql-pv.yml
5. kubectl apply -f mysql-deployment.yml
6. kubectl apply -f py-deployment.yml
7. open mysql pod: `kubectl exec -it pod/pod-name bash`
8. in termenal type  mysql -u root -p enter the password 
9. create db flaskapi
10. create table: `CREATE TABLE users(user_id INT PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(255), lastname VARCHAR(255),email VARCHAR(255), birthday VARCHAR(255));`
11. exit 
12. expose api 'minikube service flask-service'
