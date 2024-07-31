"""create channel_communication_request_mappings table

Revision ID: 7753adfcb340
Revises: 4b448322e340
Create Date: 2024-07-29 19:24:54.213771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '7753adfcb340'
down_revision: Union[str, None] = '4b448322e340'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'channel_communication_request_mappings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('communication_request_id', sa.Integer, sa.ForeignKey('communication_requests.id'), nullable=False),
        sa.Column('channel_type', sa.String(50), nullable=False),
        sa.Column('recipient', sa.String(50), nullable=False),
        sa.Column('response', sa.JSON, nullable=False),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('delivered_at', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now(),  onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('channel_communication_request_mappings')
