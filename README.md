# Welding_Management_System

//the project is based on python3, using dwebsocket and uwsgi to implement the websocket connection.

mkdir welding_management

cd welding_management

//install Mysql

sudo apt-get install mysql-server

sudo apt-get install mysql-client

sudo apt-get install libmysqlclient-dev

//check if the Mysql is installed

sudo netstat -tap | grep mysql

mysql -u root -p 
//log in

create user 'iwms'@'%' identified by '12345678'; 
//create user iwms

grant all on *.* to 'iwms'@'%'; 
//authorize iwms

create database IWMS; 
//create database

python -m venv env 
//build virtual environment for python

source env/bin/activate

pip install django==1.9 
//setup django==1.9

sudo apt install git 
//setup git

git clone https://github.com/duanhongyi/dwebsocket //download dwebsocket

cd dwebsocket

python setup.py install 
//setup dwebsocket

pip install eventlet 
//setup eventlet

sudo pip install PyMySQL 
//install PyMySQL

cd ~/Desktop/welding_management/

git clone https://github.com/DrChenchao/Welding_Management_System