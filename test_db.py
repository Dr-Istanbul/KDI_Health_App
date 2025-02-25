import asyncio
from database import engine

async def test_connection():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(lambda x: print("✅ Successfully connected to PostgreSQL!"))
    except Exception as e:
        print(f"❌ Database connection error: {e}")

asyncio.run(test_connection())

