# DVC Demo

Push the data on a remote storage

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

DVC and GitHub Actions/GitLab CI ro run a workflow

## References

https://github.com/khuyentran1401/prefect-dvc/tree/dvc_version_control

https://www.youtube.com/playlist?list=PLnK6m_JBRVNqYq2hJCspXrlLs596VDLZg

https://dvc.org/doc/start
