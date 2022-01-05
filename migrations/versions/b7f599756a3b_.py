"""empty message

Revision ID: b7f599756a3b
Revises: dd53bfb57977
Create Date: 2021-12-22 12:57:34.738083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7f599756a3b'
down_revision = 'dd53bfb57977'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uuid', sa.String(), nullable=True))
    op.create_index(op.f('ix_user_uuid'), 'user', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_uuid'), table_name='user')
    op.drop_column('user', 'uuid')
    # ### end Alembic commands ###