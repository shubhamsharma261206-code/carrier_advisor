class SearchHelper:
    """
    Helper methods for processing search results.
    """

    @staticmethod
    def extract_content(search_result: dict) -> str:
        """
        Extract only useful text content from Tavily search results.
        """

        if not search_result.get("success"):
            return "No live search results available."

        results = search_result.get("data", {}).get("results", [])

        if not results:
            return "No live search results available."

        content = []

        for item in results:

            text = item.get("content")

            if text:
                content.append(text)

        return "\n\n".join(content)