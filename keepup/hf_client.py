from huggingface_hub import InferenceClient
import os

import config.log_config as log_config
from hf_model import HfModel

HF_API_TOKEN_KEY = "HF_API_TOKEN"
HF_ENDPOINT_KEY = "HF_ENDPOINT"

logger = log_config.logger("client")


def get_inference_endpoint(repo_id: HfModel) -> InferenceClient:

    api_token = os.environ.get(HF_API_TOKEN_KEY)

    if not api_token:
        raise ValueError(f"Could not get inference endpoint client because token is not set in "
                         f"environments variable {HF_API_TOKEN_KEY}")

    return InferenceClient(token=api_token, model=repo_id.value)

