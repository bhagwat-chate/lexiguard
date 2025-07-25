# from core.validation.utils import load_llm_config
# from core.routing.llm_router import LLMRouter
# from core.logging.logger import get_logger
#
#
# def main():
#     logger = get_logger(__name__)
#     logger.info("Logger initialized in dev mode.")
#
#     # Step 1: Load YAML config
#     config = load_llm_config("shared/configs/llm_config.yml")
#
#     # Step 2: Initialize LLMRouter with config
#     llm_router = LLMRouter(config)
#
#     # Step 3: Sample prompt
#     prompt = "Explain GDPR in simple terms."
#
#     # Step 4: Call the router (will auto-pick default provider/model)
#     try:
#         response = llm_router.chat(prompt)
#         print("🔹 LLM Response:")
#         print(response)
#     except Exception as e:
#         print(f"❌ Failed to get response: {e}")
#
#
# if __name__ == '__main__':
#     main()
