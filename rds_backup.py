#!/usr/bin/python
import boto.rds
import pprint
import time
import re
import os

def touch(fname, times=None):
        with file(fname, 'a'):
                os.utime(fname, times)

directory = 'rds-snapshots/'
if not os.path.exists(directory):
        os.makedirs(directory)
dbs = [
 
]
conn = boto.rds.connect_to_region(
"us-west-1",
aws_access_key_id='',
aws_secret_access_key='')

instances = conn.get_all_dbinstances()
for db in instances:
        # Backup only main database;Skip read replicas
        dbname = str(db)[11:]
        if db.status_infos or dbname in dbs:
                print (dbname)
                if not re.findall(r"[2-9]",dbname):
                        backup_name = dbname + "-" + (time.strftime("%Y-%m-%d-%H-%M"))
                        touch(directory + backup_name + '.bak')
                        print ("Backing up db... " + backup_name)
                        db.snapshot(backup_name)
