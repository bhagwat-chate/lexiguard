# core/enums/query_parser_enums.py

from enum import Enum


class QueryType(str, Enum):
    POLICY_INTERPRETATION = "policy_interpretation"
    COMPLIANCE_CHECK = "compliance_check"
    CLAUSE_EXTRACTION = "clause_extraction"
    HALLUCINATION_ANALYSIS = "hallucination_analysis"
    MULTI_REGION_MAPPING = "multi_region_mapping"
    VERSION_DIFFERENCE = "version_difference"
    ACTIONABILITY_ANALYSIS = "actionability_analysis"


class Language(str, Enum):
    ENGLISH = "english"
    HINDI = "hindi"
    GERMAN = "german"
    FRENCH = "french"
