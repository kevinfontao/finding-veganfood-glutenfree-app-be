"""empty message

Revision ID: 8d8384da8c53
Revises: 143cf780d80e
Create Date: 2020-09-01 01:04:00.128748

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d8384da8c53'
down_revision = '143cf780d80e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('video_recipe_link', sa.String(length=120), nullable=True))
    op.drop_column('recipe', 'recipe_video_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('recipe_video_link', mysql.VARCHAR(length=120), nullable=True))
    op.drop_column('recipe', 'video_recipe_link')
    # ### end Alembic commands ###
