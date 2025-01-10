import time
from celery import Celery
from faster_whisper import WhisperModel
import requests
from tempfile import NamedTemporaryFile

celery_app = Celery(
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    broker_connection_retry_on_startup=True,
)


@celery_app.task(name="tasks.transcribe")
def transcribe(url, language):
    start_time = time.perf_counter()

    model_size = "small"  # https://github.com/SYSTRAN/faster-whisper?tab=readme-ov-file#model-conversion
    model = WhisperModel(model_size, device="cpu", compute_type="float32")

    response = requests.get(url)
    response.raise_for_status()

    with NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(response.content)
        print(temp_file.name)
        segments, _ = model.transcribe(
            temp_file.name,
            language=language,
            vad_filter=True,
            no_repeat_ngram_size=2,
        )

        transcript = [
            {
                "start": s.start,
                "end": s.end,
                "text": s.text,
            }
            for s in segments
        ]

        elapsed_time = time.perf_counter() - start_time

    return {
        "elapsed_time": f"{elapsed_time:.2f}",
        "transcript": transcript,
        "url": url,
    }
