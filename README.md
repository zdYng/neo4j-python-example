## Neo4j Movies Example Application 
### The neo4j-python  Edition

#### Stack 
* neo4j
* Flask
* Frontend: jquery, bootstrap, d3.js

#### Setup

```shell

$ git clone https://github.com/zdYng/neo4j-python-example.git

$ pip install -r movies-python-bolt/requirements

```

#### Run Example 1

You need to modify the server address / login name / password of your neo4j in test.py
``` python
## test.py
## My uri / login name / password
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("admin", "admin"))

```

Run :

```python

Guinevere
<Record friend.name='Guinevere'>
Lancelot
<Record friend.name='Lancelot'>
Merlin
<Record friend.name='Merlin'>

```


#### Run Example 2
You need to modify the server address / login name / password of your neo4j in movies-python-bolt/movies.py

``` python
## movies-python-bolt/movies.py
## My uri / login name / password
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("admin", "admin"))

```

Run

```shell
python movies-python-bolt/movies.py

# localhost:8080
```

