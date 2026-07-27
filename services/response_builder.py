from datetime import datetime


class ResponseBuilder:
    """
    Combines responses from all agents into
    one structured response.
    """

    def build(self, responses: dict) -> dict:

        final_response = {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "total_agents": len(responses),
            "agents": {},
            "summary": []
        }

        for agent_name, result in responses.items():

            if result["success"]:

                final_response["agents"][agent_name] = result["data"]

                final_response["summary"].append(
                    f"{agent_name.title()} information generated successfully."
                )

            else:

                final_response["agents"][agent_name] = {
                    "error": result["error"]
                }

                final_response["summary"].append(
                    f"{agent_name.title()} failed."
                )

        return final_response