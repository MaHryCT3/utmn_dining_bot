import sys

import httpx
from loguru import logger

from app import __version__ as bot_version


class HTTPClient:
    def __init__(self, base_url: str = '', **headers: dict) -> None:
        self.client = httpx.AsyncClient(base_url=base_url)
        self._set_default_headers(headers)

    @property
    def headers(self) -> dict:
        return self.client.headers

    @headers.setter
    def headers(self, headers: httpx._types.HeaderTypes) -> None:
        self.client.headers.update(headers)

    async def raw_request(
        self, url: str, http_method: str, query: dict | None = None, payload: dict | None = None, **kwargs
    ) -> httpx.Response:
        logger.debug(f'Send request: {http_method}: {url} | Query: {query} | Payload: {payload}')
        response = await self.client.request(
            http_method,
            url,
            params=query,
            data=payload,
            **kwargs,
        )
        logger.debug('Receive response {}: {}', response.request, response.text)
        response.raise_for_status()
        return response

    async def request_get(self, url: str, query: dict | None = None, **kwargs) -> httpx.Response:
        return await self.raw_request(url, 'GET', query=query, **kwargs)

    async def request_post(
        self, url: str, query: dict | None = None, payload: dict | None = None, **kwargs
    ) -> httpx.Response:
        return await self.raw_request(url, 'POST', query=query, payload=payload, **kwargs)

    def _set_default_headers(self, headers: dict) -> None:
        user_agent = f'DINING BOT (v{bot_version}); Python {sys.version_info.major}.{sys.version_info.minor} // HTTPX v{httpx.__version__}'
        self.client.headers.update({'User-Agent': user_agent})
        self.client.headers.update(headers)
