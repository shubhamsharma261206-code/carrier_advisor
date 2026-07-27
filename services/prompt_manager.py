class PromptManager:

    @staticmethod
    def career_prompt(career: str, search_data: str) -> str:
        return f"""
You are an expert Career Advisor.

Career:
{career}

Latest Career Information:
{search_data}

Explain in detail:

1. Career Overview
2. Roles and Responsibilities
3. Required Technical Skills
4. Soft Skills
5. Educational Qualifications
6. Top Hiring Companies

Use the latest information wherever applicable.
"""

    @staticmethod
    def salary_prompt(
        career: str,
        country: str,
        experience: str,
        search_data: str
    ) -> str:

        return f"""
You are an expert Salary Advisor.

Career:
{career}

Country:
{country}

Experience:
{experience}

Latest Salary Information:
{search_data}

Explain:

1. Fresher Salary
2. Mid-Level Salary
3. Senior Salary
4. Highest Paying Companies
5. Salary Growth
6. Factors Affecting Salary

Use the latest information wherever applicable.
"""

    @staticmethod
    def trend_prompt(career: str, search_data: str) -> str:

        return f"""
You are an expert Career Trend Analyst.

Career:
{career}

Latest Information:
{search_data}

Explain:

1. Current Job Demand
2. Future Scope
3. Hiring Trends
4. Industries Hiring
5. Automation Risk
6. Emerging Technologies

Use the latest information wherever applicable.
"""

    @staticmethod
    def roadmap_prompt(career: str, search_data: str) -> str:

        return f"""
You are an experienced Career Mentor.

Career:
{career}

Latest Career Information:
{search_data}

Create a detailed learning roadmap.

Include:

1. Beginner Stage
2. Intermediate Stage
3. Advanced Stage
4. Skills to Learn
5. Programming Languages
6. Frameworks / Tools
7. Certifications
8. Hands-on Projects
9. Portfolio Tips
10. Interview Preparation
11. Approximate Timeline

Use the latest information wherever applicable.
"""

    @staticmethod
    def interview_prompt(career: str, search_data: str) -> str:

        return f"""
You are an experienced Interview Coach.

Career:
{career}

Latest Career Information:
{search_data}

Generate:

1. Technical Interview Questions
2. HR Questions
3. Scenario-Based Questions
4. Coding Questions (if applicable)
5. Resume Tips
6. Portfolio Tips
7. Interview Strategy
8. Common Mistakes
9. Final Checklist

Use the latest information wherever applicable.
"""