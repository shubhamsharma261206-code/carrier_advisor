from tavily import TavilyClient

from config import Config


class SearchTool:
    """
    Search Tool using Tavily.

    Every agent will use this tool instead of
    calling Tavily directly.
    """

    def __init__(self):

        self.client = TavilyClient(
            api_key=Config.TAVILY_API_KEY
        )

    def search(
        self,
        query: str,
        max_results: int = None
    ) -> dict:

        if max_results is None:
            max_results = Config.MAX_SEARCH_RESULTS

        try:

            response = self.client.search(

                query=query,

                max_results=max_results,

                search_depth="advanced"

            )

            return {

                "success": True,

                "source": "tavily",

                "data": response,

                "error": None

            }

        except Exception as e:

            return {

                "success": False,

                "source": "tavily",

                "data": None,

                "error": str(e)

            }