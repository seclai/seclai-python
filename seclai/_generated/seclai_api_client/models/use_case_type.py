from enum import Enum


class UseCaseType(str, Enum):
    OTHER = "other"
    RAG_EVALUATION = "rag_evaluation"
    RESEARCH = "research"
    SEARCH_VIA_MCP = "search_via_mcp"
    SERVERLESS_RAG = "serverless_rag"

    def __str__(self) -> str:
        return str(self.value)
