"""create senders table

Revision ID: 53487415266c
Revises: 0fd1625d6e5a
Create Date: 2024-07-31 19:48:09.292712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '53487415266c'
down_revision: Union[str, None] = '0fd1625d6e5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'senders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('gateway_configuration_id', sa.Integer, sa.ForeignKey('gateway_configurations.id'), nullable=False),
        sa.Column('sender_details', sa.JSON, nullable=False),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now(),  onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('senders')
