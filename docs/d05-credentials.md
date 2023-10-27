Where to store the credentials to access either an API, a DB, or a bucket most be store in a way that the structure is share but everyone has their own credentials. 

It is suggested to keep this accesses in a file inside `config/local/credentials.yaml`.

You most follow this structure for the credentials.yaml file:

```
---
db:
  user: "user-db"
  pass: "pass-db"
  host: "host-db.com"
  port: "5432"
  db: "name-db"
s3:
  aws_access_key_id: "key-id"
  aws_secret_access_key: "secret-key"
api: 
  user: "user-api"
  pass: "pass-api"
```



The function to call this credentials is for everyone, and it is keep in `src/utils/general.py`.

