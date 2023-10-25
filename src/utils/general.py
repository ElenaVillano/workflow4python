import yaml


def read_yaml_file(yaml_file):
    """ 
    Load yaml cofigurations 
    """
    config = None
    try:
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
    except:
        raise FileNotFoundError('Couldnt load the file')

    return config


def get_s3_credentials(creds_file):
    """ 
    Get credentials for accessing AWS S3 buckets from the credentials file
    """
    
    s3_creds = read_yaml_file(creds_file)['s3']

    return s3_creds


def get_db_conn_sql_alchemy(creds_file):
    """
    Get credentials for db connection
    """
    db_creds = read_yaml_file(creds_file)['db']

    conn_db = "postgresql://{}:{}@{}:{}/{}".format(db_creds['user'],
                                                      db_creds['pass'],
                                                      db_creds['host'],
                                                      db_creds['port'],
                                                      db_creds['db'])
    return conn_db


