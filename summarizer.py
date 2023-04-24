from hf_client import get_inference_endpoint
from hf_model import HfModel

SUMMARY_TEXT_KEY = "summary_text"


class Summarizer:
    def __init__(self, model: HfModel = HfModel.BART_LARGE_CNN):
        self.summarizer = get_inference_endpoint(repo_id=model)

    def summarize(self, text: str, min_length: int = 30, max_length: int = 200):
        params = {"min_length": min_length, "max_length": max_length}

        return self.summarizer(text, params)[0].get(SUMMARY_TEXT_KEY)
