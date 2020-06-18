# Articles API Final project of Udacity Course


## API Article

### Installing Dependencies
#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviorment 

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup
With Postgres running, restore a database using the Articles.psql file provided.  terminal run:

```
psql -U postgres
create database databasename'
```

``` bash
psql -d databasename  -U postgres -a -f Articles.psql

```

- Can use this code for export your postgres database

```
pg_dump -U server_name original_database > anyname.psql
```

## Running the server

- To run the server in linux os, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
- To run the server in Windows execute:

- cmd

```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
- powershall
```
$env:FLASK_APP=app.py 
$env:FLASK_ENV="development" 
flask run
```
-git bash
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## API Reference

### Getting Started
Base URL: At present this app be run remotley and is  hosted as a base URL. The backend app is hosted at the default, https://lolo94.herokuapp.com/.
Authentication: This version of the application does  require  auth0 authentication.

### Getting Started
Errors are returned as JSON objects in the following format:

The API will return four error types when requests fail:

 1. 404: resource not found

 ```
 {
    "success": False, 
    "error": 404,
    "message": "resource not found"
}
 ```

 2. 422: Not Processable

 ```
 {
     "success":False,
     "error":422,
     "message": "unprocessable"
}
 ```
 3. Unauthorized

 ```
 {
    "success": False, 
    "error": 401,
    "message": "Unauthorized"
}
 ```
 4. Forbidden
 ```
 {
    "success": False, 
    "error": 403,
    "message": "Forbidden"
}
 ```

### Endpoints

#### GET '/welcome'


```
curl https://lolo94.herokuapp.com/welcome
```

```
{
  "welcome": "you can do with this api (get person, get article, post person, post article, patch person, patch article, delete person, delete article"
}
```


#### GET '/person'
- permission requirement (get:person)
- Access to all persons info such as name and departments.

'curl -H "Authorization: bearer  <ACCESS_TOKEN>" https://lolo94.herokuapp.com/person'

##### Example

```curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw" https://lolo94.herokuapp.com/person```

##### response

```
  "person": [
    {
      "department": "Network",
      "id": 5,
      "name": "Yaseein"
    },
    {
      "department": "Software",
      "id": 7,
      "name": "Ibrahim"
    },
    {
      "department": "network",
      "id": 9,
      "name": "dddd"
    },
    {
      "department": "Software",
      "id": 2,
      "name": "sososososososososososososososo"
    }
  ],
  "success": true
}

```

#### Get '/article'
- permission requirement (get:article)
- Access to all articles info such as data, category, and person's id who write article.

'curl -H "Authorization: bearer  <ACCESS_TOKEN>" http://127.0.0.1:5000/article'

##### Example
```curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw" https://lolo94.herokuapp.com/article```

##### Response
```
  "articles": [
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 1,
      "person_id": 2
    },
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 2,
      "person_id": 5
    },
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 3,
      "person_id": 9
    }
  ],
  "success": true
}

```


#### post '/person'
- permission requirement (post:person)
- post new person.

`curl -H "Authorization: bearer <token>  https://lolo94.herokuapp.com/person -X POST -H "Content-Type: application/json" -d '{"name":"areeg fahad","department":"network"}'`

##### Example

```
curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw"  https://lolo94.herokuapp.com/person -X POST -H "Content-Type: application/json" -d '{"name":"areeg fahad","department":"network"}'
```
##### Response
  "person": [
    {
      "department": "network",
      "id": 52,
      "name": "areeg fahad"
    },
    {
      "department": "Network",
      "id": 5,
      "name": "Yaseein"
    },
    {
      "department": "Software",
      "id": 7,
      "name": "Ibrahim"
    },
    {
      "department": "network",
      "id": 9,
      "name": "dddd"
    },
    {
      "department": "Software",
      "id": 2,
      "name": "sososososososososososososososo"
    }
  ],
  "success": true
}

#### post '/article'
- permission requirement (post:article)
- post new article.

`curl -H "Authorization: bearer <token>  https://lolo94.herokuapp.com/article -X POST -H "Content-Type: application/json" -d '{"name":"areeg fahad","category":"network", "person_id":2}'`
##### Example
```curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw"  https://lolo94.herokuapp.com/article -X POST -H "Content-Type: application/json" -d '{"data":"areeg fahad","category":"network","person_id":"2"}'

```
##### Response 

``` "article": [
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 1,
      "person_id": 2
    },
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 2,
      "person_id": 5
    },
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 3,
      "person_id": 9
    },
    {
      "category": "network",
      "data": "areeg fahad",
      "id": 48,
      "person_id": null
    }
  ],
  "success": true
}

```


#### patch '/person'
- permission requirement (patch:person)
- Modify one or more fields in person info.

`curl -H "Authorization: bearer <token>  https://lolo94.herokuapp.com/person -X POST -H "Content-Type: application/json" -d '{"name":"areeg fahad","department":"network"}'`

##### Example

```
curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw"  https://lolo94.herokuapp.com/person/2 -X patch -H "Content-Type: application/json" -d '{"name":"areeg fahad"}'

```
##### Response
```
  "persons": [
    {
      "department": "network",
      "id": 52,
      "name": "areeg fahad"
    },
    {
      "department": "Software",
      "id": 2,
      "name": "areeg fahad"
    },
    {
      "department": "Network",
      "id": 5,
      "name": "Yaseein"
    },
    {
      "department": "Software",
      "id": 7,
      "name": "Ibrahim"
    },
    {
      "department": "network",
      "id": 9,
      "name": "dddd"
    }
  ],
  "success": true
}
```



#### patch '/article'
- permission requirement (patch:article)
- Modify one or more fields in person info.

`curl -H "Authorization: bearer <token>  https://lolo94.herokuapp.com/article/1 -X patch -H "Content-Type: application/json" -d '{"data":"abcd"}'`

##### Example
``` curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw" https://lolo94.herokuapp.com/article/2 -X patch -H "Content-Type: application/json" -d '{"data":"abcd"}'

```

##### Response

```
  "articles": [
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 1,
      "person_id": 2
    },
    {
      "category": "Network",
      "data": "Lorem wincluding versions of Lorem Ipsum.Lorem\n\t\t\tIpsum is simply dummy text of the printing and typesetting industry",
      "id": 3,
      "person_id": 9
    },
    {
      "category": "network",
      "data": "areeg fahad",
      "id": 48,
      "person_id": null
    },
    {
      "category": "Network",
      "data": "abcd",
      "id": 2,
      "person_id": 5
    }
  ],
  "success": true
}

```

#### delete '/person'
- permission requirement (delete:person)
- Delete person.

`curl -H "Authorization: bearer <token>  https://lolo94.herokuapp.com/person/1 -X DELETE -H`

##### Example

```curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw"  https://lolo94.herokuapp.com/person/2 -X DELETE

```
##### Response 

```
{
  "deleted_id": "2",
  "success": true
}

```

#### delete '/article'
- permission requirement (delete:article)
- Delete article.

`curl -H "Authorization: bearer <token>  https://lolo94.herokuapp.com/person/1 -X DELETE -H`

##### Example

```curl -H "Authorization: bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikx3clNxYXNfR1p3NXJUZGw0cXdCZCJ9.eyJpc3MiOiJodHRwczovL2Rldi01d2dncWhidC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlNTAzMGQ3NzFiMjUwYjc3MTY3NTM2IiwiYXVkIjoicHJvamVjdCIsImlhdCI6MTU5MjQyOTIwMywiZXhwIjoxNTkyNTE1NjAzLCJhenAiOiJWMWFyUXBVdzRrZGJKc3k2MDNQQ1Q2cUdyeVFydmo5cCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFydGljbGUiLCJkZWxldGU6cGVyc29uIiwiZ2V0OmFydGljbGVzIiwiZ2V0OnBlcnNvbnMiLCJwYXRjaDphcnRpY2xlIiwicGF0Y2g6cGVyc29uIiwicG9zdDphcnRpY2xlIiwicG9zdDpwZXJzb24iXX0.a9W8xZQjSUNcLvym_w9iRIFRyWkUcCOcVWQnH8NFXPRdWBpnOKRbP4Ji6YdHq2j9dl9Ywr1u5UksV7ZRIS9hFpbiiRnfACQabL2ShTm3eOR-GyH1F8xZpZrF02m9O4qpZVJRq6SUaIY5OoxkmoumbD7fGJlcy74t22F35EWDBsVsNmXnzUIxADRyBgZnlJBh3Tr_QcILUpHr8HfdEzwQiauWcK9Z8vCVzAdnUULcyhGBYaas_mgCpj6fJWndyYn-ZfeY1ACHEceZ_Tgkg_NRb9RmhsTFD76TYq8ZAimupFHsVCMnB_mlRIf4mGmPfDgJlOWHvtxFypSsR_PjSRyrgw"  https://lolo94.herokuapp.com/article/2 -X DELETE

```
##### Respone

```
{
  "deleted_id": "2",
  "success": true
}

```

## Testing
To run the tests, run

```
python test_flaskr.py
```

# Author AREEG FAHAD
