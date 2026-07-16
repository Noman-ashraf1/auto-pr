from app.infrastructure.llm.openai_client import OpenAICompatibleClient


class LLMReviewService:

    def __init__(
        self,
        client: OpenAICompatibleClient,
    ):
        self.client = client

    async def review(
        self,
        pull_request: dict,
        changed_files: list,
        findings: list,
    ) -> str:

        prompt = self._build_prompt(
            pull_request,
            changed_files,
            findings,
        )

        return await self.client.generate(prompt)

    def _build_prompt(
        self,
        pr,
        files,
        findings,
    ):

        return f"""
You are a Senior Staff Software Engineer.

Review this GitHub Pull Request.

Title:
{pr["title"]}

Changed Files:
{len(files)}

Static Findings:
{len(findings)}

Review for:

- Bugs
- Security
- Performance
- Architecture
- Best Practices
- Maintainability

Return Markdown.
"""