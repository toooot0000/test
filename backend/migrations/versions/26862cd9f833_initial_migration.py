"""Initial migration.

Revision ID: 26862cd9f833
Revises: 
Create Date: 2021-01-15 17:56:47.455610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26862cd9f833'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.Column('urgency', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
