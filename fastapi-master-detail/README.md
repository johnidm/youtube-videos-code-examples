## FastAPI Rest example master/detail

The example developed in this repo has the goal to demonstrate master-detail concept in an API Rest.

The **logs** endpoints family list a logs file in a specific directory and provide details about the log file content.

The master–detail is a concept that provides a list of records + details for the currently selected item.

In this project a list of records can be get by `logs` endpoint and the details can be gt by `logs/{item-name}`.

### Install dependences

```
pip install -r requirements.txt
```

### Run application

```
uvicorn main:app
```

### Endpoint

- http://0.0.0.0:8000/
- http://0.0.0.0:8000/logs/