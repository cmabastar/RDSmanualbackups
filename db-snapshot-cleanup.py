#!/usr/bin/python
import boto.rds2
import pprint
import time
import glob
import ntpath
import re
import datetime

DAYS_EXPIRE = 90

# Get all the filenames
dirfiles = glob.glob('./rds-snapshots/*.bak')
filenames = []

# Clear up extensions
for files in dirfiles:
        file = ntpath.basename(files).split('.')[0] #Remove .bak extension
        filenames.append(file)

conn = boto.rds2.connect_to_region(
"us-west-1",
aws_access_key_id='',
aws_secret_access_key='')

snapshots = conn.describe_db_snapshots()
list_snapshots = snapshots['DescribeDBSnapshotsResponse']['DescribeDBSnapshotsResult']['DBSnapshots']
for snap in list_snapshots:
        if snap['SnapshotType'] == 'automated':
                continue
        dbs_id = snap['DBSnapshotIdentifier']
        delta_date = datetime.timedelta(days=DAYS_EXPIRE)
        acceptable_date = datetime.datetime.now() - delta_date
        if dbs_id in filenames:
                datestr =  re.search(r'\d{4}-\d{2}-\d{2}-\d{4}$', dbs_id).group()
                date_object = datetime.datetime.strptime(datestr, '%Y-%m-%d-%H%M')
                if (date_object < acceptable_date):
                        # Delete it here
                        print "Deleting expired snapshot... " + dbs_id
                        conn.delete_db_snapshot('rds-man-snapshot-2014-03-07-0439')
                        # Remove the files
                        os.remove('./rds-snapshots/' + dbs_id)
