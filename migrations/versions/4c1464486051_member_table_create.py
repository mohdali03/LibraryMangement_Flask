"""member table create

Revision ID: 4c1464486051
Revises: 
Create Date: 2025-01-27 12:19:51.699383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c1464486051'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'library_members',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('contact', sa.String(length=100), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('register_date', sa.DateTime, nullable=False, default=sa.func.current_timestamp()),
        sa.Column('password', sa.String(length=250), nullable=False),
        sa.Column('is_admin', sa.Boolean, nullable=False, default=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('library_members')
    # ### end Alembic commands ###

