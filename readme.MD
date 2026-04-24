# 주제
- kafka

# repo
- https://github.com/edu-kenshi/kafka-local.git

# 설치
```
    docker compose up -d
```

# 패키지 설치
```
pip install kafka-python
```

# CLI 모드로 테스트
```
# 접속
# 호스트  PC
PS ~\kafka-local> docker container exec -it kafka bash

# 컨테이너
root@4527e52ba5f6:/# pwd
/
root@4527e52ba5f6:/# cd /opt/kafka/bin

# 토픽 생성
# 파티션 1개로 관리, 복제본 1개로 관리되는 토픽 구성
> kafka-topics.sh --create --topic spacex --bootstrap-server 127.0.0.1:9092 --partitions 1 --replication-factor 1

# 토픽 전송(프로듀서)
> kafka-console-producer.sh --topic spacex --bootstrap-server 127.0.0.1:9092

# 컨슈머
> kafka-console-consumer.sh --topic spacex --bootstrap-server 127.0.0.1:9092

```

# local-datapipline 목표 시스템
```
[ LAYER ]          [ COMPONENT ]              [ PROTOCOL / ACTION ]             [ DATA FORMAT ]
====================================================================================================
SOURCE       :     Python (log_gen.py)  ----( Write to File )---->  [ /sensor_logs/*.log ]
               |                                                                   |
               |                                                            ( Shared Volume )
               v                                                                   |
INGESTION    :     Fluent Bit (Agent)   <---( Tailing File  )----------------------+
               |          |
               |          | [ CHANNEL A: DIRECT BYPASS ]
               |          +--------------------------------------------( Produce )--+
               |          |                                                         |
               |          | [ CHANNEL B: PROXY ROUTE  ]                             |
               |          +----( Forward )----> [ Logstash ] ----( Produce )--+     |
               |                                     |                        |     |
               v                                     v                        v     v
TRANSFORM    : (A: Bypass)  +--[ Grok    : Pattern Matching & Extract Fields   ]--+ |
               |            +--[ Mutate  : Data Type Conversion (Str->Float)   ]--+ |
               |            +--[ Tagging : Add Metadata for Conditional Alerts ]--+ |
               |                                                              |     |
MESSAGING    :     Kafka / MSK (Broker) <-------------------------------------+-----+
               |          |             ( Merge Structured & Processed Data )
               |          |
               |          +----( Topic A: factory-json-topic ) <--- [Channel A Result]
               |          +----( Topic B: factory-text-topic ) <--- [Channel B Result]
               v                                                               |
VISUALIZE    :     OpenSearch (DB)      <---( Indexing & Search )---->  DASHBOARD (Kibana)
====================================================================================================
```

# 프로젝트 재구성
- docker-compose.yaml 수정 (KRaft 적용된)
```
    docker compose down
    docker compose up -d
```