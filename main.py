# main.py

from core.logging.logger import get_logger
from shared.configs.py_loader.config_loader import load_environment
from core.agents.query_parser_agent import QueryParserAgent

load_environment('dev')


def main():
    logger = get_logger(__name__)
    logger.info("Logger initialized in dev mode.")

    # Step 2: Initialize LLMRouter with config
    query_parser_agent_obj = QueryParserAgent(query="What is the capital of India?")
    response = query_parser_agent_obj.process_query()
    print(f"agent: query parser response: {response}")


if __name__ == '__main__':
    main()
