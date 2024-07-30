"""create gateway_configurations table

Revision ID: 42de75bee3f1
Revises: 6106a8ffeaa2
Create Date: 2024-07-29 19:24:53.698533

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42de75bee3f1'
down_revision: Union[str, None] = '6106a8ffeaa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'gateway_configurations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('account_id', sa.Integer, sa.ForeignKey('accounts.id'), nullable=False),
        sa.Column('gateway_id', sa.Integer, sa.ForeignKey('gateways.id'), nullable=False),
        sa.Column('configuration_details', sa.JSON, nullable=False),
        sa.Column('status_id', sa.JSON, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('gateway_configurations')
