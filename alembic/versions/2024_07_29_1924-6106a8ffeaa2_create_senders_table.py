"""create senders table

Revision ID: 6106a8ffeaa2
Revises: 54a2bb05ed3a
Create Date: 2024-07-29 19:24:53.528844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6106a8ffeaa2'
down_revision: Union[str, None] = '54a2bb05ed3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'senders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('configuration_id', sa.Integer, sa.ForeignKey('gateway_configurations.id'), nullable=False),
        sa.Column('sender_details', sa.JSON, nullable=False),
        sa.Column('configuration_details', sa.JSON, nullable=False),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('senders')
