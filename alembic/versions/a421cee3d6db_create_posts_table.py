"""create_posts_table

Revision ID: a421cee3d6db
Revises: 
Create Date: 2023-09-22 19:27:05.189383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a421cee3d6db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts_table',
                    sa.Column('post_id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('title', sa.String(), nullable = False),
                    )
    pass


def downgrade():
    op.drop_table('posts_table')
    pass
