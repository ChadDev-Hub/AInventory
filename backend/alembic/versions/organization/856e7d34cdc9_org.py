"""org

Revision ID: 856e7d34cdc9
Revises: 88d1ddaafb2d
Create Date: 2026-11-03 23:07:36.553261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '856e7d34cdc9'
down_revision: Union[str, Sequence[str], None] = '88d1ddaafb2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE SCHEMA organization if not exists;")

    op.create_table(
        "companies",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(),
            nullable=False,
            primary_key=True,
        ),
        sa.Column(
            "name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "address",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "geometry",
            sa
        )

    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
