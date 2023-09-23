"""add userid to posts table with relation to userstable

Revision ID: 50cdddafce74
Revises: 4c56a51f9961
Create Date: 2023-09-23 13:00:28.412422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50cdddafce74'
down_revision = '4c56a51f9961'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts_table', sa.Column('user_id', sa.Integer(), nullable = False))
    # create_foreign_key( <name_of_foreign_key>, <source_table>, <target_table>, <left_column>, <right_column>, ondelete )
    op.create_foreign_key('posts_users_userid_fkey', source_table='posts_table', referent_table='users_table',
                          local_cols=['user_id'], remote_cols=['user_id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_userid_fkey', table_name='posts_table')
    op.drop_column('posts_table', 'user_id')
    pass
