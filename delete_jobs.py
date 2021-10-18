import os
import subprocess
import json
import glob
import yaml
import copy
import shelve
import pprint

job_db = shelve.open('jobs_database', writeback=True)

cmd = 'databricks jobs delete --job-id '

print("Deleting all jobs in the jobs database")
print("--------------------------------------")
for elem in job_db['jobs']:
    print("Deleting job ",elem)
    os.system(cmd + str(elem))

del job_db['jobs']
job_db.close()
