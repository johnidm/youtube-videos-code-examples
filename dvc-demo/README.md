# DVC Demo

DVC (Data Version Control) is a tool designed to handle data and model versioning for machine learning projects.

Main Features:

- Data and Model Versioning (push and pull to a storage)
- Pipelines (steps)
- Experiment Tracking (params and metrics)
- Integration with Git and CI/CD

## MLOps Stages

- Data Versioning & Management
- Pipeline Orchestration & Automation
- Experiment Tracking & Model Registry
- Model Serving & Deployment (CI/CD)
- Monitoring & Observability

## Pushing

Push the data on a remote storage

```
dvc add data/data.csv
dvc add model/model.pkl
```

```
dvc remote add local /tmp/dvc-storage
dvc push -r local
```

``` 
dvc remote add s3 (google drive/S3/GCP Storage, DagsHub, etc)
dvc push -r s3
dvc pull -r s3
``` 

```
dvc repro
```

## DVC and GitHub Actions/GitLab CI ro run a workflow

Steps 

- Pull the data from DVC 
- Run the pipeline
- Push the model to DVC
- Commit the changes
- Push to Git remote repo

## Commands 

- dvc dag (show the pipeline in a graph)
- dvc update
- dvc import
- dvc params diff
- dvc metrics diff
- dvc plots 

## First steps

Initialize DVC (dvc init) adn Git (git init)

Create a data directory and a data.txt file, or grab the data from a remote storage (dvc get https://github.com/johnidm/dvc-demo/tree/main/data/data.txt -o data/data.txt)

Add the data directory to DVC (dvc add data/data.txt)

Commit the changes (git add . && git commit -m "Add data"). Include the DVC files (config, lock, .dvc)

Push the changes to the remote repo (git push)

Add a remote storage (dvc remote add -d storage gdrive://109dis99...)

Push the data to DVC (dvc push -r storage)

## Next Steps

- Add a metrics to the pipeline
- Add params to the pipeline
- Store the data and the model on a remote storage (Data/Model Registry)
- Experimetn tracking

## References

https://github.com/khuyentran1401/prefect-dvc/tree/dvc_version_control

https://www.youtube.com/playlist?list=PLnK6m_JBRVNqYq2hJCspXrlLs596VDLZg

https://dvc.org/doc/start

https://www.youtube.com/watch?v=TNW5KyFAy8U

https://www.youtube.com/watch?v=kLKBcPonMYw

https://cml.dev/

https://dvc.org/doc/use-cases/data-registry/tutorial

https://github.com/iterative/example-get-started-experiments

https://www.youtube.com/watch?v=iduHPtBncBk

https://dvc.org/doc/studio
