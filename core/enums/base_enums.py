from enum import Enum


class Jurisdiction(str, Enum):
    GDPR = 'gdpr'
    HIPPA = 'hippa'
    DPDP = 'dpdp'
    AI_ACT = 'ai_act'


class OutputFormat(str, Enum):
    TEXT = 'text'
    JSON = 'json'
    MARKDOWN = 'markdown'
