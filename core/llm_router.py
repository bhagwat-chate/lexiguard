import os
import yaml
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

# --- Load config ---
CONFIG_PATH = "configs/llm_config.yml"
with open(CONFIG_PATH, "r") as f:
    LLM_CONFIG = yaml.safe_load(f)

# --- Vendor LLM Clients (simplified placeholders) ---
from openai import OpenAI
from cohere import Client as CohereClient
from anthropic import Anthropic
from google.generativeai import GenerativeModel
from huggingface_hub import InferenceClient


# --- LLM Router Class ---
class LLMRouter:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.default_provider = config["default_provider"]
        self.models = self._load_all_clients(config)

    def _load_all_clients(self, config):
        clients = {}

        for provider, data in config["providers"].items():
            key = os.getenv(data.get("api_key") or data.get("access_token"))
            if provider == "openai":
                clients[provider] = OpenAI(api_key=key)
            elif provider == "cohere":
                clients[provider] = CohereClient(api_key=key)
            elif provider == "anthropic":
                clients[provider] = Anthropic(api_key=key)
            elif provider == "gemini":
                import google.generativeai as genai
                genai.configure(api_key=key)
                clients[provider] = genai
            elif provider == "huggingface":
                clients[provider] = InferenceClient(token=key)

        return clients

    def get_model(self, provider: str, model_name: str):
        if provider == "openai":
            return lambda prompt: self.models[provider].chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            ).choices[0].message.content

        elif provider == "cohere":
            return lambda prompt: self.models[provider].chat(message=prompt, model=model_name).text

        elif provider == "anthropic":
            return lambda prompt: self.models[provider].messages.create(
                model=model_name,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            ).content[0].text

        elif provider == "gemini":
            return lambda prompt: self.models[provider].GenerativeModel(model_name).generate_content(prompt).text

        elif provider == "huggingface":
            return lambda prompt: self.models[provider].text_generation(prompt=prompt, model=model_name)

    def chat(self, prompt: str, preferred_provider: str = None, model_name: str = None):
        provider = preferred_provider or self.default_provider
        model = model_name or self.config["providers"][provider]["models"][0]["name"]

        try:
            handler = self.get_model(provider, model)
            return handler(prompt)
        except Exception as e:
            fallback = self._get_fallback_provider(provider, model)
            if fallback:
                print(f"[Router] Primary failed, using fallback: {fallback}")
                return self.chat(prompt, preferred_provider=fallback)
            else:
                raise RuntimeError(f"[Router] Failed to fetch LLM response: {str(e)}")

    def _get_fallback_provider(self, provider: str, model_name: str):
        models = self.config["providers"][provider].get("models", [])
        for model in models:
            if isinstance(model, dict) and model.get("name") == model_name:
                return model.get("fallback")
        return None
