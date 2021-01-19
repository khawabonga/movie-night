"""empty message

Revision ID: 05e9b26af975
Revises: 
Create Date: 2021-01-19 11:54:17.132919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05e9b26af975'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('imdb_id', sa.Integer(), nullable=True),
    sa.Column('cover_url', sa.String(length=240), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_movies_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_movies')),
    sa.UniqueConstraint('imdb_id', name=op.f('uq_movies_imdb_id')),
    sa.UniqueConstraint('title', name=op.f('uq_movies_title'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_table('user')
    # ### end Alembic commands ###