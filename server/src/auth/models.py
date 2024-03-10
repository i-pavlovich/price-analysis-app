from datetime import datetime
from typing import Optional

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(75), unique=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    password: Mapped[str] = mapped_column()

    name: Mapped[Optional[str]] = mapped_column(String(75))
    surname: Mapped[Optional[str]] = mapped_column(String(75))

    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=datetime.utcnow)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
