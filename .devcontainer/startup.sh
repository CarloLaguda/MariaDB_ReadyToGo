sudo apt update
sudo apt install mariadb-server -y
sudo service mariadb start
sudo mariadb
CREATE USER IF NOT EXIST 'pythonuser'@'localhost' IDENTIFIED BY 'prova56__';
GRANT ALL PRIVILEGES ON *.* TO 'pythonuser'@'localhost' WITH GRANT OPTION;
exit
pip install mysql
#sudo npm install -g @angular/cli