"""create templates table

Revision ID: c9111dffcd3b
Revises: 53487415266c
Create Date: 2024-07-31 19:48:09.468576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'c9111dffcd3b'
down_revision: Union[str, None] = '53487415266c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'templates',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('channel_type', sa.String(50), nullable=False),
        sa.Column('content', sa.Text),
        sa.Column('description', sa.String(50)),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now(),  onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('templates')
