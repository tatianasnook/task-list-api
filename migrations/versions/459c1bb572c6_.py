"""empty message

Revision ID: 459c1bb572c6
Revises: 80dbd23f6f4e
Create Date: 2024-11-05 17:12:24.976567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '459c1bb572c6'
down_revision = '80dbd23f6f4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
