from sqlalchemy.ext.asyncio import AsyncSession

from app.Models.product import Product


class ProductRepository:

    async def create_product(self, session: AsyncSession, product: ProductCreate) -> Product:
