# Motivation

Provide as simple as possible approach to using Django authentication db. Currently only sqlite3 supported.

# Installation

1. git clone radicale-django-sqlite3-auth
2. cd radicale-django-sqlite3-auth
3. pip --upgrade . 
4. edit `config` for radicale 

```
cat config
[auth]
type = radicale-django-sqlite3-auth
django_sqlite3_path = /path/to/your/db.sqlite3
```
5. run `radicale --config /path/to/your/config`
6. you should see in debug logs 
```
[7f7cc6e4e700] INFO: Using sqllite3: /path/to/your/db.sqlite3
[7f7cc6e4e700] INFO: Successful login: 'django_user'
```
7. in that case 'django_user' was successfully autheticated.
