"""add users table

Revision ID: 4c56a51f9961
Revises: 0492c6357b47
Create Date: 2023-09-23 12:51:06.089315

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4c56a51f9961'
down_revision = '0492c6357b47'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users_table',
                    sa.Column('user_id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('email', sa.String(), nullable = False, unique = True),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default = sa.text('Now()')))
    pass


def downgrade():
    op.drop_table('users_table')
    pass
