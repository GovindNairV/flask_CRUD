# Flask API

This is a basic Flask app to perform CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using PyMongo library.


## Requirements


To run this app on your local machine, make sure the following dependencies are installed on your local machine:
1. Docker
2. Docker Compose
3. Postman (for testing)
4. MongoDB Compass (for GUI to interact with mongodb)

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/GovindNairV/flask_CRUD.git
```

Go to the project directory

```bash
  cd flask_CRUD
```

Run the app with docker compose

```bash
  docker-compose up --build
```

Stop the app with the following command

```bash
  docker-compose down
```


## API Reference

### Get all users

```http
  GET http://localhost:5001/users
```

**Example**
![GET all](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/GET_all.png?raw=true)

### Get user with specified ID

```http
  GET http://localhost:5001/users/${id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

**Example**
![GET user with specified ID](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/GET_id.png?raw=true)


### Create a new user with specified data

```http
  POST http://localhost:5001/users
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. User Name |
| `email` | `string` | **Required**. User email |
| `pwd` | `string` | **Required**. User password |

**Request Example:**
```json
{
    "name": "govind",
    "email": "govind@gmail.com",
    "pwd": "password"
}
```

**Example**
![POST Create a new user](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/POST.png?raw=true)
![POST Create a new user output](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/POST_output.png?raw=true)

### Update the user with specified ID with new data

```http
  PUT http://localhost:5001/users/${id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**. Id of item to update |
| `name` | `string` | **Required**. User Name |
| `email` | `string` | **Required**. User email |
| `pwd` | `string` | **Required**. User password |

**Request Example:**
```json
{
    "name": "govind",
    "email": "govind@gmail.com",
    "pwd": "password"
}
```

**Example**
![PUT Update a user](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/PUT.png?raw=true)
![PUT Update a user output](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/PUT_output.png?raw=true)

### Delete the user with specified ID

```http
  DELETE http://localhost:5001/users/${id}
```

**Example**
![DELETE a user](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/DELETE.png?raw=true)
![DELETE a user output](https://github.com/GovindNairV/flask_CRUD/blob/main/Screenshots/DELETE_output.png?raw=true)

