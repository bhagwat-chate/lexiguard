import os
import yaml


def load_agent_llm_config(path="shared/configs/yml_configs/agent_llm_config.yml"):
    """
    Load the agent vendor llm config file
    :param path: agent vendor llm confile file path in project
    :return: agent vendor llm confile
    : on error: error
    """
    try:
        path = os.path.join(os.getcwd(), path)

        with open(path, "r") as f:
            return yaml.safe_load(f)

    except Exception as e:
        print(f"agent_llm_config.yml file not found at: {path}")
        raise e
