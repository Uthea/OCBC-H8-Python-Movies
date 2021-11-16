"""remove books

Revision ID: d0c01f072d4a
Revises: af73669bfa70
Create Date: 2021-11-16 06:49:09.029667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0c01f072d4a'
down_revision = 'af73669bfa70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=25), nullable=False),
    sa.Column('author', sa.VARCHAR(length=40), nullable=False),
    sa.Column('date_added', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
