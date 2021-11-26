# web3django
## web3.py para django 
### instalacion del proyecto 

#### preparar carpeta para proyecto / dentro de carpeta 
1. pipenv install
2. pipenv shell 
3. pipenv install django 
4. pip install web3 

#### preparar django 
1. django-admin startproject "nombre proyecto"
2. crear carpeta para las /apps i crear archivo __init__.py en la carpeta /apps para que django acepte la carpeta
3. django-admin startapp "nombreapp" en la carpeta apps

#### configurar base de datos 
1. en preparacion 



#### configuracion de infura api para ethereum
1. crear cuenta en infura https://infura.io/
2. from web3 import Web3 
3. infura_url = "https://mainnet.infura.io/v3/a85133a2396a4ec599f76c3fafbcd161"
4. web3 = Web3(Web3.HTTPProvider(infura_url))
5. provar coneccion en un prompt de python con web3.isConnected()