"""Create Sender Table

Revision ID: 16407c09e1cc
Revises: b918c98d132e
Create Date: 2024-08-12 20:01:10.223052

"""
from __future__ import annotations

from typing import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '16407c09e1cc'
down_revision: str | None = 'b918c98d132e'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Use the existing 'status' enum type, so do not create it again
    status_enum = ENUM('ACTIVE', 'INACTIVE', name='status', create_type=False)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'senders', sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('gateway_configuration_id', sa.Integer(), nullable=False),
        sa.Column('sender_details', sa.JSON(), nullable=False),
        sa.Column('status', status_enum, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ['gateway_configuration_id'],
            ['gateway_configurations.id'],
        ), sa.PrimaryKeyConstraint('id'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('senders')
    # ### end Alembic commands ###
