from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("admin", "admin"))


def add_friend(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)


def print_friends_of(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) "
                         "WHERE a.name=$name "
                         "RETURN friend.name ORDER BY friend.name", name=name):
        print(record["friend.name"])
        print(record)

with driver.session() as session:
    session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arthur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    session.read_transaction(print_friends_of, "Arthur")

# driver.close()