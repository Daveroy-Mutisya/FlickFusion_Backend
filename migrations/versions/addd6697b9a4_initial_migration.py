"""Initial migration

Revision ID: addd6697b9a4
Revises: 
Create Date: 2024-04-16 19:46:21.083610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'addd6697b9a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('poster', sa.String(length=255), nullable=True),
    sa.Column('trailer_url', sa.String(length=255), nullable=False),
    sa.Column('genre', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('gmail', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Ontheatre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.Column('seats', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('rating_theater', sa.Float(), nullable=True),
    sa.Column('poster_theater', sa.String(length=255), nullable=True),
    sa.Column('trailer_url_theater', sa.String(length=255), nullable=False),
    sa.Column('genre_theater', sa.String(length=50), nullable=True),
    sa.Column('price_theater', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_movie_association',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_movie_association')
    op.drop_table('Ontheatre')
    op.drop_table('users')
    op.drop_table('movies')
    # ### end Alembic commands ###
