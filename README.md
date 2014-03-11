RDSmanualbackups
================

Automated Manual RDS Backups


How to use:
Provide access key/id and update the dbs array for whitelisted names of database. The script is intended to snapshot from the master.

====

    python rds_backup.py
  
This script will create an rds-snapshots/ folder and create a filename of the database snapshot to be created.



Cleanup old snapshots
====

    python db-snapshot-cleanup.py
    

This is related to the rds_backup.py. Base on the files created in 'rds-snapshots/' folder. It will remove all databases that is more than 90 days old (can be configurable) 
