"""Create Gateway Table

Revision ID: 5cb23f1d2ac4
Revises: d3429ea1bad6
Create Date: 2024-08-12 13:53:33.966161

"""
from __future__ import annotations

from typing import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '5cb23f1d2ac4'
down_revision: str | None = 'd3429ea1bad6'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Use the existing 'status' enum type, so do not create it again
    status_enum = ENUM('ACTIVE', 'INACTIVE', name='status', create_type=False)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'gateways', sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('channel_type',
                  sa.Enum('WHATSAPP',
                          'EMAIL',
                          'SMS',
                          'IVR',
                          'APP_NOTIFICATION',
                          name='channeltype'),
                  nullable=False),
        sa.Column('status', status_enum, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('name'),
        sa.UniqueConstraint('name', 'channel_type',
                            name='uq_name_channel_type'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gateways')
    # ### end Alembic commands ###
