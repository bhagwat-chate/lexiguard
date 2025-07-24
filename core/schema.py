from typing import Optional
from pydantic import BaseModel
from core.enums import RiskLevelEnum
from core.enums import ActorEnum


class ClauseMetaData(BaseModel):
    law_name: str
    jurisdiction: str
    clause_number: Optional[str]
    clause_text: str


class ComplianceResponse(BaseModel):
    law_reference: ClauseMetaData
    risk_level: RiskLevelEnum
    recommendation: str
    responsible_actor: ActorEnum
    disclaimer: str = "This is not legal advice. Please consult with legal counsel."
