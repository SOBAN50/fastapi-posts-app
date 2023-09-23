"""add content column to posts table

Revision ID: 0492c6357b47
Revises: a421cee3d6db
Create Date: 2023-09-22 22:51:53.486615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0492c6357b47'
down_revision = 'a421cee3d6db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_table',
                  sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts_table', 'content')
    pass
