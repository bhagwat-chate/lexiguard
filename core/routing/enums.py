from enum import Enum


class RiskLevelEnum(str, Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'


class ActorEnum(str, Enum):
    DPO = 'Data Protection Officer'
    LEGAL_TEAM = 'Legal Team'
    TECH_TEAM = 'Tech Team'
    LEADERSHIP = 'Leadership'


class Jurisdiction(str, Enum):
    GDPR = 'GDPR'
    HIPAA = 'HIPAA'
    DPDP = 'DPDP'
    CCPA = 'CCPA'
