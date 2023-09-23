"""add test column to posts table

Revision ID: b480b56e8770
Revises: 06afb56712d3
Create Date: 2023-09-23 16:02:01.717056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b480b56e8770'
down_revision = '06afb56712d3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_table', sa.Column('test_col', sa.String(), nullable = True))
    pass


def downgrade():
    op.drop_column('posts_table', 'test_col')
    pass
