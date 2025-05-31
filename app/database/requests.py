from app.database.models import async_session
from app.database.models import User, Review
from sqlalchemy import select


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()
        

async def add_review(user_id: int, text: str) -> None:
    async with async_session() as session:
        session.add(Review(user_id=user_id, textreview=text))
        await session.commit()