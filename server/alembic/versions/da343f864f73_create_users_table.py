"""create users table

Revision ID: da343f864f73
Revises: 
Create Date: 2023-09-16 15:56:55.086776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da343f864f73'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('login', sa.String(20), nullable=False),
        sa.Column('password', sa.String(20), nullable=False)
    )

def downgrade():
    op.drop_table('users')