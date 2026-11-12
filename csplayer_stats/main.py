from apify import Actor
from crawlee.crawlers import BeautifulSoupCrawler
from crawlee.http_clients import CurlImpersonateHttpClient
from .routes import router

async def main() -> None:
    """The crawler entry point."""
    async with Actor:
        crawler = BeautifulSoupCrawler(
            request_handler=router,
            max_requests_per_crawl=10,
            http_client=CurlImpersonateHttpClient(),
        )


        await crawler.run(
            [
                'https://crawlee.dev',
            ]
        )
