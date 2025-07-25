# core/routing/llm_fallback_router.py

from core.logging.logger import get_logger
from core.routing.router_clients import get_openai_client, get_cohere_client, get_gemini_client, get_huggingface_client

log = get_logger(__name__)


class LLMFallbackRouter:

    def execute_with_fallback(self, agent_name, agent_config, query):
        try:
            fallback_order = agent_config.get('fallback_order', [])
            all_llms = agent_config.get('llms', [])
            strategy = agent_config.get('fallback_strategy', 'fast')

            for provider in fallback_order:
                for llm in all_llms:

                    if llm['provider'] != provider:
                        continue

                    model = llm['model']
                    try:
                        log.info(f"{agent_name} trying '{provider}' with '{model}'")

                        while model is not None:
                            try:
                                client_fn = self.get_client_fn(provider, model, agent_config)
                                return client_fn(query)
                            except Exception as e:
                                log.warning(f"{provider} - {model} failed: {str(e)}")
                                model = llm.get('fallback')

                    except Exception as e:
                        log.warning(f"[{agent_name}] {provider} - {model} failed: {str(e)} ")
                        if strategy == 'strict':
                            break
            raise RuntimeError(f"[{agent_name}] all fallbacks failed.")

        except Exception as e:
            log.warning(f"[{agent_name}] critical failure in fallback execution: {str(e)}")
            raise e

    def get_client_fn(self, provider: str, model_name: str, config: dict):
        client_map = {
            "openai": get_openai_client,
            "cohere": get_cohere_client,
            "gemini": get_gemini_client,
            "huggingface": get_huggingface_client,
        }

        if provider not in client_map:
            raise ValueError(f"Unsupported provider '{provider}' in agent config")

        return client_map[provider](model_name, config)

