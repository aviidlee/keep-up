from huggingface_hub import InferenceApi
import os

import log_config
from hf_model import HfModel

HF_API_TOKEN_KEY = "HF_API_TOKEN"
HF_ENDPOINT_KEY = "HF_ENDPOINT"

logger = log_config.logger("client")


def get_inference_endpoint(repo_id: HfModel) -> InferenceApi:
    api_token = os.environ.get(HF_API_TOKEN_KEY)

    if not api_token:
        raise ValueError(f"Could not get inference endpoint client because token is not set in "
                         f"environments variable {HF_API_TOKEN_KEY})")

    return InferenceApi(repo_id=repo_id.value, token=api_token)

