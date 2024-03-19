from flask_sqlalchemy import SQLAlchemy

"""
docker run -idt -p 3306:3306 --privileged=true \
-e TZ=Asia/Shanghai \
-e MYSQL_DATABASE=open-password-mysql \
-e MYSQL_ROOT_PASSWORD=pdBGKGjRyX3Jb2Hn \
--name open-password-mysql mysql:8.0.20
"""
base_db = SQLAlchemy()
