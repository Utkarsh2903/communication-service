"""create accounts table

Revision ID: 54a2bb05ed3a
Revises: 
Create Date: 2024-07-29 19:24:53.360219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54a2bb05ed3a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('sub_tenant_id', sa.Integer, nullable=False),
        sa.Column('api_key', sa.Text, nullable=False, unique=True),
        sa.Column('status_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=func.now(),  onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('accounts')
