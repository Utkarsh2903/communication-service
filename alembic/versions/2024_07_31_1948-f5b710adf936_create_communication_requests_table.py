"""create communication_requests table

Revision ID: f5b710adf936
Revises: c9111dffcd3b
Create Date: 2024-07-31 19:48:09.642598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'f5b710adf936'
down_revision: Union[str, None] = 'c9111dffcd3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'communication_requests',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('request_id', sa.String(50), nullable=False),
        sa.Column('template_id', sa.Integer, sa.ForeignKey('templates.id'), nullable=False),
        sa.Column('sender_id', sa.Integer, sa.ForeignKey('senders.id'), nullable=False),
        sa.Column('request_params', sa.JSON, nullable=False),
        sa.Column('channel_type', sa.String(50), nullable=False),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('callback_url', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now(),  onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('communication_requests')
