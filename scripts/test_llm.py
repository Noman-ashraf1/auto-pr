import asyncio

from app.infrastructure.llm.openai_client import OpenAICompatibleClient
from app.infrastructure.llm.review_service import LLMReviewService


async def main():

    client = OpenAICompatibleClient(
        base_url="http://35.253.171.20:8080/v1",
        api_key="imiashrafnomiashrafhussaini203147415272",
        model="Qwen3-VL",
    )

    service = LLMReviewService(client)

    review = await service.review(
        pull_request={
            "title": "Initial implementation of Autonomous AI Code Review System"
        },
        changed_files=[],
        findings=[],
    )

    print(review)


asyncio.run(main())