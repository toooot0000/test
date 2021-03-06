"""empty message

Revision ID: 64cf493a9949
Revises: 26862cd9f833
Create Date: 2021-01-18 10:11:24.522648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64cf493a9949'
down_revision = '26862cd9f833'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('state', sa.Enum('undue', 'completed', 'overdue', 'deleted', name='todosates'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'state')
    # ### end Alembic commands ###
