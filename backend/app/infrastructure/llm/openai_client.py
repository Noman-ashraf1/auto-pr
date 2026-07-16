from openai import AsyncOpenAI


class OpenAICompatibleClient:

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str,
    ):
        self.model = model

        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
        )

    async def generate(
        self,
        prompt: str,
    ) -> str:

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content