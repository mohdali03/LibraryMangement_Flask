"""alter table of library members 

Revision ID: 4bae26530481
Revises: 3ac2faf1698b
Create Date: 2025-01-27 12:36:15.961003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bae26530481'
down_revision: Union[str, None] = '3ac2faf1698b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('library_members', 'is_admin', existing_type=sa.Boolean(), server_default=sa.false())


def downgrade() -> None:
    pass
