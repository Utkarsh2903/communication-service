"""create communication_requests table

Revision ID: 4b448322e340
Revises: fbfa478c547f
Create Date: 2024-07-29 19:24:54.042094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b448322e340'
down_revision: Union[str, None] = 'fbfa478c547f'
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
        sa.Column('status_id', sa.String(50), nullable=False),
        sa.Column('callback_url', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('communication_requests')
