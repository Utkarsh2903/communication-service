"""create gateways table

Revision ID: 788c34ee853a
Revises: a62f374a311b
Create Date: 2024-07-31 19:48:08.940470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '788c34ee853a'
down_revision: Union[str, None] = 'a62f374a311b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'gateways',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('channel_type', sa.String(50), nullable=False),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now(),  onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('gateways')
