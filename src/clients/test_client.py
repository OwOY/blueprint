from httpx import AsyncClient


class TestClient:
    def __init__(self, client: AsyncClient):
        self.client = client
        
    async def get_data(self):
        response = await self.client.get(
            '/url', # 這裡設定外部的連結,
            headers = {} # 設定 headers
        )
        return response
    
    