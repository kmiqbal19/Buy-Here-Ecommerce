"""initial migration

Revision ID: 933edbadabe8
Revises: 
Create Date: 2023-06-13 23:07:32.441148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '933edbadabe8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('register', schema=None) as batch_op:
        batch_op.add_column(sa.Column('f_name', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('register', schema=None) as batch_op:
        batch_op.drop_column('f_name')

    # ### end Alembic commands ###