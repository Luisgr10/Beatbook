"""empty message

Revision ID: e8be3c046809
Revises: 95f4b5e06b7d
Create Date: 2024-04-21 11:41:14.655444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8be3c046809'
down_revision = '95f4b5e06b7d'
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
