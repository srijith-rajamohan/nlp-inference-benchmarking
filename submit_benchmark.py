import os
import subprocess
import json
import glob
import yaml
import copy
import shelve
import pprint

command = '/Users/srijith.rajamohan/opt/anaconda3/bin/databricks jobs create --json-file '
job_list = []

for files in glob.glob('./job_json/cpu_jobs/*.json'):
      print("Submitting job for file %s ... " %(files))
      proc = subprocess.Popen(command + files, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
      tmp = proc.stdout.read()
      print(tmp)
      job_id = json.loads(tmp)['job_id']
      proc = subprocess.Popen('/Users/srijith.rajamohan/opt/anaconda3/bin/databricks jobs run-now --job-id '+ str(job_id), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
      tmp = json.loads(proc.stdout.read())
      print('Job submitted with id ',job_id)
      print('Run for job scheduled, received run id ',tmp['run_id'],' and job number ',tmp['number_in_job'])
      print('\n----------------------------------------------------\n')
      job_list.append(job_id)

job_db = shelve.open('jobs_database', writeback=True)
if job_db.get('jobs'):
    job_db['jobs'].extend(job_list)
else:
    job_db['jobs'] = job_list
job_db.close()
