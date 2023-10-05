# MiniBloggingApp-test

> A mini blogging application built using Django RestAPI.

## Getting started

If you're just getting started, make sure you have the latest version of [Python](https://www.python.org/downloads/) installed.

- Clone the repository into a folder of your choosing and change directory into the folder MiniBloggingApp-test.
```sh
cd MiniBloggingApp-test
```

Then run the following commands in succession.

#### Activate Virtual Environment
```sh
pipenv shell
```
#### Install Requirements

```sh
pip install -r requirements.txt
```

The included sqlite database has all the necessary data as such theirs no need for running migrations.

Initialie the server to view the RestAPI data.

```sh
python manage.py runserver 8000
```
### Fetch all blog posts
  <img src="https://github.com/Clemo97/MiniBloggingApp-test/blob/main/screenshots/blog-1.png" alt="rest api home page 1" />

### Fetch a single blog post by ID
<img src="https://github.com/Clemo97/MiniBloggingApp-test/blob/main/screenshots/blog-2.png" alt="rest api home page 2" />

## Token 
Some routes are protected using token-based authentication.

## :books: Documentation

- See the documentation site 
  (http://localhost:8000/swagger/)

<img src="https://github.com/Clemo97/MiniBloggingApp-test/blob/main/screenshots/blog-3.png" alt="rest api home page 3" />

The interactive redoc documentations is here (http://localhost:8000/redoc/)

<img src="https://github.com/Clemo97/MiniBloggingApp-test/blob/main/screenshots/blog-4.png" alt="rest api home page 4" />


### Bonus (Optional)

- [ ] Implement caching.
- [x] Consume the API using a console command.
- [ ] Write unit tests for the applica/on.
- [X] Use Docker to containerize the applica/on.

