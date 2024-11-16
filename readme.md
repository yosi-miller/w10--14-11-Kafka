# Enemy Email Monitoring System

## Project description

<div dir="rtl">

מערכת לניטור הודעות אימייל המיועדת לזהות תוכן חשוד בזמן אמת. המערכת מבצעת:
1. עיבוד הודעות בפורמט JSON.
2. זיהוי מילות מפתח חשודות כמו "hostage" או "explos".
3. שליחה של הודעות חשודות ל-Kafka לנושאים ייעודיים.
4. שמירת תוכן חשוד במאגרי PostgreSQL ו-MongoDB.
5. סידור מחדש של משפטים כך שהמסוכן ביותר יופיע בראש הרשימה.
</div>


## To run the project
### navigate to the venv 
```bash
.\.venv\Scripts\activate
```
### Installation all dependencies
```bash
pip install -r requirements.txt
```
### Installation separately dependencies
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
- to run the docker dependencies (After then change the port database to the cornet ports)
```bash
docker-compose up -d
```

___
<h2>Shows the project flow</h2>
<img src="readme item/Untitled video - Made with Clipchamp.gif" alt="Alt Text" width="600" />

<h2>Review of the main project components </h2>
<img src="readme item/review_project.png" alt="Alt Text" width="1000" />

<h2>The main function to found the dangerous words in the sentences emails</h2>
<img src="readme item/function_dangerous_sentences_checker.png" alt="Alt Text" width="800" />

---

<h2>More common commands</h2>

- access the kafka container bash (change to the current container name)

```bash
docker exec -it testpreparationproject-kafka-1 bash
```

- Containers name (Ex.)

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