"""add remaining poststable columns

Revision ID: 06afb56712d3
Revises: 50cdddafce74
Create Date: 2023-09-23 13:12:22.203085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06afb56712d3'
down_revision = '50cdddafce74'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_table',
                  sa.Column('published', sa.Boolean(), nullable = False, server_default = 'TRUE'))
    op.add_column('posts_table',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default = sa.text('Now()')))
    pass


def downgrade():
    op.drop_column('posts_table', 'published')
    op.drop_column('posts_table', 'created_at')
    pass
