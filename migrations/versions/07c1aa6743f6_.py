"""empty message

Revision ID: 07c1aa6743f6
Revises: 
Create Date: 2024-05-15 14:26:28.857625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07c1aa6743f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('musical_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('address', sa.String(length=500), nullable=False),
    sa.Column('phone', sa.String(length=500), nullable=True),
    sa.Column('profile_picture', sa.String(length=500), nullable=True),
    sa.Column('banner_picture', sa.String(length=500), nullable=True),
    sa.Column('instagram', sa.String(length=500), nullable=True),
    sa.Column('tiktok', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('email', sa.String(length=500), nullable=False),
    sa.Column('username', sa.String(length=500), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('gender', sa.String(length=500), nullable=True),
    sa.Column('city', sa.String(length=500), nullable=True),
    sa.Column('profile_image_url', sa.String(length=500), nullable=True),
    sa.Column('banner_picture', sa.String(length=500), nullable=True),
    sa.Column('instagram', sa.String(length=500), nullable=True),
    sa.Column('tiktok', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('band',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('profile_picture', sa.String(length=500), nullable=True),
    sa.Column('banner_picture', sa.String(length=500), nullable=True),
    sa.Column('instagram', sa.String(length=500), nullable=True),
    sa.Column('tiktok', sa.String(length=500), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_favorite_category',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('musical_category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['musical_category_id'], ['musical_category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'musical_category_id')
    )
    op.create_table('band_members',
    sa.Column('band_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['band_id'], ['band.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('band_musical_category',
    sa.Column('band_id', sa.Integer(), nullable=False),
    sa.Column('musical_category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['band.id'], ),
    sa.ForeignKeyConstraint(['musical_category_id'], ['musical_category.id'], ),
    sa.PrimaryKeyConstraint('band_id', 'musical_category_id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('address', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('picture_url', sa.String(length=500), nullable=True),
    sa.Column('instagram', sa.String(length=500), nullable=True),
    sa.Column('tiktok', sa.String(length=500), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('place_id', sa.Integer(), nullable=True),
    sa.Column('band_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['band_id'], ['band.id'], ),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['place_id'], ['place.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('assistance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('band_events',
    sa.Column('band_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['band.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('band_id', 'event_id')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=500), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('media')
    op.drop_table('band_events')
    op.drop_table('assistance')
    op.drop_table('event')
    op.drop_table('band_musical_category')
    op.drop_table('band_members')
    op.drop_table('user_favorite_category')
    op.drop_table('band')
    op.drop_table('user')
    op.drop_table('place')
    op.drop_table('musical_category')
    # ### end Alembic commands ###
