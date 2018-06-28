"""Change attribute password

Revision ID: 2413d22265ca
Revises: 8d937ca2fde6
Create Date: 2018-06-25 16:48:32.036622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2413d22265ca'
down_revision = '8d937ca2fde6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=100), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###