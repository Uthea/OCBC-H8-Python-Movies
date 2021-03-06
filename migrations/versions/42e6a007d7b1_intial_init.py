"""intial init

Revision ID: 42e6a007d7b1
Revises: 
Create Date: 2021-11-16 15:00:58.812589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42e6a007d7b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('department', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tokenlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=1000), nullable=False),
    sa.Column('refresh_token', sa.String(length=1000), nullable=False),
    sa.Column('used', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=1000), nullable=True),
    sa.Column('username', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_title', sa.String(length=1000), nullable=False),
    sa.Column('budget', sa.BIGINT(), nullable=True),
    sa.Column('popularity', sa.BIGINT(), nullable=True),
    sa.Column('release_date', sa.String(length=1000), nullable=False),
    sa.Column('revenue', sa.BIGINT(), nullable=True),
    sa.Column('title', sa.String(length=1000), nullable=False),
    sa.Column('vote_average', sa.REAL(), nullable=True),
    sa.Column('vote_count', sa.BIGINT(), nullable=True),
    sa.Column('overview', sa.String(length=1000), nullable=False),
    sa.Column('tagline', sa.String(length=1000), nullable=False),
    sa.Column('uid', sa.BIGINT(), nullable=True),
    sa.Column('director_id', sa.BIGINT(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['directors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('user')
    op.drop_table('tokenlist')
    op.drop_table('directors')
    # ### end Alembic commands ###
