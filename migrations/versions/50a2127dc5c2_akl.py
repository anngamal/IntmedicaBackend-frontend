"""akl

Revision ID: 50a2127dc5c2
Revises: 0a7998f022c9
Create Date: 2023-10-27 14:22:16.770541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50a2127dc5c2'
down_revision = '0a7998f022c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('electrotherapy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))
        batch_op.drop_column('image_url')

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('image')

    with op.batch_alter_table('electrotherapy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('image')

    # ### end Alembic commands ###
