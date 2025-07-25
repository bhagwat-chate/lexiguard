# core/routing/vendor_clients.py

import os
from openai import OpenAI
from cohere import Client as CohereClient
from anthropic import Anthropic
from huggingface_hub import InferenceClient
import google.generativeai as genai


def get_openai_client(model_name, config):
    key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=key)

    return lambda prompt: client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=config.get("temperature", 0.2),
        top_p=config.get("top_p", 0.85),
        max_tokens=config.get("max_tokens", 512)
    ).choices[0].message.content


def get_cohere_client(model_name, config):
    key = os.getenv("COHERE_API_KEY")
    client = CohereClient(api_key=key)

    return lambda prompt: client.chat(
        message=prompt,
        model=model_name,
        temperature=config.get("temperature", 0.2)
    ).text


def get_anthropic_client(model_name, config):
    key = os.getenv("ANTHROPIC_API_KEY")
    client = Anthropic(api_key=key)

    return lambda prompt: client.messages.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=config.get("max_tokens", 512)
    ).content[0].text


def get_gemini_client(model_name, config):
    key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=key)

    return lambda prompt: genai.GenerativeModel(model_name).generate_content(prompt).text


def get_huggingface_client(model_name, config):
    key = os.getenv("HF_API_KEY")
    client = InferenceClient(token=key)

    return lambda prompt: client.text_generation(prompt=prompt, model=model_name)
