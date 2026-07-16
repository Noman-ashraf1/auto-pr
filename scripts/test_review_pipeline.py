import asyncio

from app.application.pipelines.review_pipeline import ReviewPipeline


async def main():

    pipeline = ReviewPipeline()

    findings = await pipeline.run(
        owner="Noman-ashraf1",
        repo="auto-pr",
        number=1,
    )

    print(f"\nTotal Findings: {len(findings)}\n")

    for finding in findings:

        print(finding.title)
        print(finding.file_path)
        print(finding.severity.value)

        print("-" * 50)


asyncio.run(main())