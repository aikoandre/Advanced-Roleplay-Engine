"""Message

Revision ID: ec761a02fa6a
Revises: e9ea008b21f6
Create Date: 2025-05-24 12:34:39.748650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision: str = 'ec761a02fa6a'
down_revision: Union[str, None] = 'e9ea008b21f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('global_lore', schema=None) as batch_op:
        batch_op.drop_index('ix_global_lore_title')

    op.drop_table('global_lore')
    with op.batch_alter_table('chat_messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_beginning_message', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat_messages', schema=None) as batch_op:
        batch_op.drop_column('is_beginning_message')

    op.create_table('global_lore',
    sa.Column('id', sa.CHAR(length=32), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('tags', sqlite.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('global_lore', schema=None) as batch_op:
        batch_op.create_index('ix_global_lore_title', ['title'], unique=False)

    # ### end Alembic commands ###
