"""akl

Revision ID: a2984adafbdf
Revises: 00b95129235b
Create Date: 2023-10-27 14:03:11.576360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2984adafbdf'
down_revision = '00b95129235b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('electrotherapy', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    with op.batch_alter_table('powerdotProducts', schema=None) as batch_op:
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    with op.batch_alter_table('recoverythermProducts', schema=None) as batch_op:
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    with op.batch_alter_table('theracupProducts', schema=None) as batch_op:
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    with op.batch_alter_table('therafaceProducts', schema=None) as batch_op:
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    with op.batch_alter_table('theragunProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
        batch_op.drop_column('href')
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    with op.batch_alter_table('waveseriesProducts', schema=None) as batch_op:
        batch_op.drop_column('description_url')
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('waveseriesProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('theragunProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('href', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('description')

    with op.batch_alter_table('therafaceProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('theracupProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('recoverythermProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('recoveryairProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('description')

    with op.batch_alter_table('powerdotProducts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description_url', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('electrotherapy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
