import aiohttp
import asyncio
import redis
import boto3
from tqdm import tqdm


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        results = []
        for url in tqdm(urls):
            async with session.get(url) as resp:
                results.append(await resp.text())
        return results


def get_redis_client():
    return redis.Redis(host="localhost", port=6379)


def get_s3_client():
    return boto3.client("s3")
