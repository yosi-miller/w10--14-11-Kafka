### navigate to the venv 
```bash
.\.venv\Scripts\activate
```

## installation dependencies
#### To install kafka
```bash
pip install kafka-python
```
#### To install pymongo
```bash
pip install pymongo
```
#### To install flask
```bash
pip install Flask
```

## Docker actions
- to run the docker dependencies
```bash
docker-compose up -d
```

- access the kafka container bash (change to the current container name)
```bash
docker exec -it testpreparationproject-kafka-1 bash
```
- Containers name
```
 Container w10--14-11-kafka-db-sql-1                                                                                                                                                                                 1.7s 
 Container w10--14-11-kafka-mongodb-1                                                                                                                                                                                1.7s 
 Container w10--14-11-kafka-zookeeper-1                                                                                                                                                                              1.7s 
 Container w10--14-11-kafka-kafka-1  
```

## Kafka actions
- create the topic (change to the current topic name)

```bash
kafka-topics --create --topic transaction-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

### how do i know what topics do i have?
```bash
kafka-topics --list --bootstrap-server localhost:9092
```

- Run specifically file 
```bash
python str_consumer.py
```