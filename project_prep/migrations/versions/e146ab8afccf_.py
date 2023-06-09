"""empty message

Revision ID: e146ab8afccf
Revises: ecedc12de335
Create Date: 2023-05-06 09:38:33.216590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e146ab8afccf'
down_revision = 'ecedc12de335'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
