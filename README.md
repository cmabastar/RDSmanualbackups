
## AWS RDS Automated Manual Backups
A python boto automated manual rds backups

### Dependencies
		boto.rds2


### Automated Manual RDS Backups
When to use it when there's an automated snapshot?

In cases of accidental deletion of RDS instance, the automated snapshots are also gone and there's no way to recover. This script will be doing manual snapshots and will only be deleted when the admin specifically deletes the rds snapshots.

### How to use:
Provide access key/id and update the dbs array for whitelisted names of database. The script is intended to snapshot from the master.



    python rds_backup.py
  
This script will create an rds-snapshots/ folder and create a filename of the database snapshot to be created.



### Cleanup old snapshots

    python db-snapshot-cleanup.py
    

This is related to the rds_backup.py. Base on the files created in 'rds-snapshots/' folder. It will remove all databases that is more than 90 days old (can be configurable) 
