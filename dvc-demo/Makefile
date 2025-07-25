.PHONY: install push run-pipeline

install:
	pip install -r requirements.txt

push:
	dvc push -r local

pull:
	dvc pull -r local

run-pipeline: push
	dvc repro
