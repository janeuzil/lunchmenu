# lunchmenu

[Cisco Spark Bot](https://developer.ciscospark.com/bots.html)  which gives you the daily menu from your favourite restaurant:
- leverages the [node-sparkbot](https://github.com/CiscoDevNet/node-sparkbot#readme) API
- leverages the [Zomato](https://developers.zomato.com/documentation) API
- leverages the [Google Translate](https://cloud.google.com/translate/docs/) API


## Installation
Open the terminal on your machine (e.g. Ubuntu) and install required packages:
```bash
$ sudo apt-get install mysql-server python-pip docker.io
```

Create a new root password for the MySQL database if it does not exist:
```bash
$ mysqladmin -u root password "********";
```
Connect to MySQL database:
```bash
$ mysql -u root -p
```
Create a new database with user for the Spark bot (in this example we will use database **lunchmenu** and user **lunchmenu**):
```sql
CREATE DATABASE lunchmenu;
CREATE USER 'lunchmenu'@'localhost' IDENTIFIED BY '**********';
GRANT ALL ON lunchmenu.* TO 'lunchmenu'@'localhost';
FLUSH PRIVILEGES;
```
Modify configuration file that mysql will listen also on 127.0.0.1 address which will be used with Docker connectivity:
```bash
$ vim /etc/mysql/my.cnf
```
Uncomment or put this line into the configuration file:
```bash
bind-address = 127.0.0.1
```
Restart the MySQL server:
```bash
# /etc/init.d/mysql restart
```

## Configuration
Create a simple Bash script with environmental variables which will help you to run the server in the Docker:
```bash
$ touch run.sh
$ chmod +x run.sh
```
Edit the file with the following lines (Note: Do not forget to change the password):
```bash
#!/bin/bash

sudo docker run -d -ti \
-e LUNCHMENU_URL="https://janeuzil.cz/api/lunchmenu" \
-e SPARK_ACCESS_TOKEN="*************************" \
-e DB_HOST="127.0.0.1" \
-e DB_NAME="lunchmenu" \
-e DB_USER="lunchmenu" \
-e DB_PASSWD="*******" \
-p 8081:8081 \
--net=host \
--name lunchmenu \
lunchmenu:latest
```
**Note:** Docker needs root privileges as it needs to access the kernel space.

## Running
Build the Docker image based on the Dockerfile:
```bash
$ sudo docker build -t lunchmenu .
```
Simply run your created Bash script:
```bash
$ ./run.sh
```

## Tunneling
In this section there are described methods if you do not have public URL, or you are behind corporate firewall or proxy.

### Port 8081
You can allow the port 8081 on your local server using uncomplicated firewall utility:
```bash
# ufw allow 8081/tcp
```

### HTTPS
If you are running Apache on your server and you do not want to open the port 8081, you can use **http_proxy** module to redirect the traffic on given URL to your moderator bot. First enable the Apache module:
```bash
# a2enmod proxy_http
# cd /etc/apache2/sites-enabled/
```
Then edit the appropriate configuration file, where you listen to port 443 (e.g. 000-default-le-ssl.conf), with the following line:
```apacheconfig
<IfModule mod_ssl.c>
<VirtualHost *:443>
        .
        .
        .
        ProxyPass "/api/lunchmenu" "http://localhost:8081/api/lunchmenu"
        .
</VirtualHost>
```
Restart the Apache server:
```bash
# /etc/init.d/apache2 restart
```
You should get the JSON health-check using following URL - https://example.com/api/lunchmenu

### Public URL
If you do not have a public URL, but you are running on the local computer, you can use [NGROK](https://ngrok.com). Simply download the binary to your machine and run the following command:
```bash
$ ./ngrok http 8081
```
You will get random public URL (e.g. https://a1b2c3.ngrok.io/) which you can use as the **LUNCHMENU_URL** variable in your local running script.

