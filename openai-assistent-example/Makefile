run-web:
	streamlit run web/app.py --server.runOnSave true

run-api:
	fastapi dev api/main.py

install-dependecies:
	pip install -r web/requirements.txt

docker-push-chat-web:
	@docker build -f Dockerfile -t openai-assistent-example .	
