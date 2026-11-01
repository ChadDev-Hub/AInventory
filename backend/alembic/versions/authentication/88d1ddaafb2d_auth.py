"""authentication

Revision ID: 88d1ddaafb2d
Revises: 
Create Date: 2026-11-01 23:57:48.473492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88d1ddaafb2d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # CREATE IDENTITY SCHEMA
    op.execute(
    """CREATE schema if not exists auth;
    """
    )

    # ==========================================
    # ROLES
    # ==========================================
    op.create_table(
        "roles",
        sa.Column(
            "id",
            sa.SmallInteger(),
            sa.Identity(),
            primary_key=True
        ),
        sa.Column(
            "name",
            sa.String(50),
            nullable=False
        ),
        sa.Column(
            "description",
            sa.String(255),
            nullable=True
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),
        sa.UniqueConstraint("name", name="uq_auth_roles_name"),
        schema="auth"
    )

    # ==========================================
    # USERS
    # ==========================================
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("gen_random_uuid()"),
            primary_key=True
        ),
        sa.Column(
            "email",
            sa.String(255),
            nullable=False
        ),
        sa.Column(
            "username",
            sa.String(100),
            nullable=True
        ),
        sa.Column(
            "password_hash",
            sa.String(255),
            nullable=True
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.true(),
            nullable=False
        ),
        sa.Column(
            "last_login",
            sa.DateTime(timezone=True),
            nullable=True
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),
        sa.UniqueConstraint("username", name="uq_auth_users_username"),
        schema="auth"
    )

    # ==========================================
    # USER ROLES (MANY-TO-MANY)
    # ==========================================
    op.create_table(
        "user_roles",
        sa.Column(
            "user_id",
            sa.Uuid(),
            sa.ForeignKey("auth.users.id", ondelete="CASCADE"),
            primary_key=True
        ),
        sa.Column(
            "role_id",
            sa.SmallInteger(),
            sa.ForeignKey("auth.roles.id", ondelete="CASCADE"),
            primary_key=True
        ),
        sa.Column(
            "assigned_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),
        schema="auth"
    )

    # ==========================================
    # USER PROFILES
    # ==========================================
    op.create_table(
        "profiles",
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("gen_random_uuid()"),
            primary_key=True
        ),
        sa.Column(
            "user_id",
            sa.Uuid(),
            sa.ForeignKey("auth.users.id", ondelete="CASCADE"),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "first_name",
            sa.String(100),
            nullable=True
        ),
        sa.Column(
            "middle_name",
            sa.String(100),
            nullable=True
        ),
        sa.Column(
            "last_name",
            sa.String(100),
            nullable=True
        ),
        sa.Column(
            "phone_number",
            sa.String(30),
            nullable=True
        ),
        sa.Column(
            "avatar_url",
            sa.Text(),
            nullable=True
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        ),
        schema="auth"
    )

    
    


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
    """DROP schema if exists auth;
    """
    )
