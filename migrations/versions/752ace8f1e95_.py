"""empty message

Revision ID: 752ace8f1e95
Revises: 
Create Date: 2020-10-21 08:30:44.007569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '752ace8f1e95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_info', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_info', 'email')
    # ### end Alembic commands ###
