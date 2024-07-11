"""Add role column to users table

Revision ID: cfdf261191fb
Revises: 7d98437b9907
Create Date: 2024-07-10 13:15:37.566877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfdf261191fb'
down_revision: Union[str, None] = '7d98437b9907'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users', 
        sa.Column('role', sa.String(length=50), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('users', 'role')
