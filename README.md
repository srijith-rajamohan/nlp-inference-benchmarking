
## About

This repository contains code to run and time inference on an task for various cluster configurations (both CPU and GPUs) on Databricks.

### Job Runners 

This repository contains the job runner file 'submit_benchmark.py' to run the code for NLP inference on GPUs and CPUs. The cluster configurations are in the folder job_json/ and the notebooks to performs inference are in the folder /notebooks. The job ids can be logged to a 'shelve' database locally, and deleted from the job queue on Databricks by running 'delete_jobs.py'.


