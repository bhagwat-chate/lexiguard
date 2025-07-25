import yaml
from functools import lru_cache
from dotenv import load_dotenv
from pathlib import Path
from core.logging.logger import get_logger

log = get_logger(__name__)


@lru_cache(maxsize=None)
def load_environment(env_name: str = "dev") -> None:
    """
    Loads environment variables from .env.local files inside the `env/` directory at the project root.

    Args:
        env_name (str): Target environment. Allowed values = {"local", "dev", "qa", "stage", "prod"}

    Raises:
        FileNotFoundError: If the corresponding .env.local file does not exist.
        ValueError: If env_name is not one of the supported environments.
    """

    allowed_envs = {"local", "dev", "qa", "stage", "prod"}
    env_name = env_name.lower().strip()

    if env_name not in allowed_envs:
        log.error(f"[ENV LOAD ERROR] Unsupported environment: {env_name}. Allowed: {allowed_envs}")
        raise ValueError(f"[ENV LOAD ERROR] Unsupported environment: {env_name}. Allowed: {allowed_envs}")

    # Compose relative path to env file
    env_file = ".env.dev" if env_name == 'dev' else f".env.{env_name}"
    env_path = Path(__file__).resolve().parent.parent / "env" / env_file

    if not env_path.exists():
        log.error(f"[ENV LOAD ERROR] File not found: {env_path}")
        raise FileNotFoundError(f"[ENV LOAD ERROR] File not found: {env_path}")

    load_dotenv(dotenv_path=env_path, override=True)
    log.info(f"[ENV LOAD] success: {env_name}")


@lru_cache()
def load_config(relative_path: str) -> dict:
    """load the LLM client config from YAML file"""

    base_dir = Path(__file__).resolve().parent.parent  # Adjust according to your file's nesting
    file_path = base_dir / relative_path

    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found at: {file_path}")

    with file_path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)
