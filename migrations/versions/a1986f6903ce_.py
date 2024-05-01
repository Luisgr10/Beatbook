"""empty message

Revision ID: a1986f6903ce
Revises: a40104d672ea
Create Date: 2024-04-22 16:11:48.710386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1986f6903ce'
down_revision = 'a40104d672ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_band_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(None, ['created_band_id'])
        batch_op.create_foreign_key(None, 'band', ['created_band_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('created_band_id')

    # ### end Alembic commands ###
