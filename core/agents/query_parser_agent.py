# core/agents/query_parser_agent.py

# from core.routing.agent_llm_router import AgentLLMRouter
from core.validation.utils import load_agent_llm_config
from core.routing.llm_fallback_router import LLMFallbackRouter
from core.logging.logger import get_logger

log = get_logger(__name__)


class QueryParserAgent:

    def __init__(self, query):
        self.query = query
        self.fallback_handler_obj = LLMFallbackRouter()

    def process_query(self):
        try:
            log.info('QueryParserAgent.process_query.EXECUTION_start')

            # agent_llm_router_obj = AgentLLMRouter(agent_name='query_parser')
            # agent_config = agent_llm_router_obj.get_agent_llm_config()

            all_agent_config = load_agent_llm_config()
            agent_config = all_agent_config["agents"]['query_parser']

            response = self.fallback_handler_obj.execute_with_fallback(agent_name='query_parser',
                                                                       agent_config=agent_config,
                                                                       query=self.query)

            log.info('QueryParserAgent.process_query.EXECUTION_END')

            return response

        except Exception as e:
            print(f"ERROR: {e}")
            raise e
