# How to work with users and credentials 

A suggested place to store credentials, keys or tokens to access either an API, a DB, or a bucket is in `config/local/credentials.yaml`.

In this file, you store the information to access some service required in your Python pipeline. This file doesn't upload to the repository because it is placed at the `.gitignore` file. The idea is that all collaborators have their own access keys, but you all have the same structure to run the code.

Be carefull never uploading the credentials file and always have in your repository a `.gitignore` file. 

The structure for the credentials.yaml file:

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


The function to call this credentials is keep in `src/utils/general.py`.

