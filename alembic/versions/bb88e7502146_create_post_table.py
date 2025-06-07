"""create post table

Revision ID: bb88e7502146
Revises: 
Create Date: 2025-06-07 10:08:33.825031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb88e7502146'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table('post', sa.Column('id',sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    
    op.drop_table('post')
    
    pass
