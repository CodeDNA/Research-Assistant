from pydantic import BaseModel, Field
class SearchQuery(BaseModel):
    search_query: str = Field("", description="Search query for retrieval.")