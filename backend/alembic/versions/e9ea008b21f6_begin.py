"""Begin

Revision ID: e9ea008b21f6
Revises: 
Create Date: 2025-05-23 20:37:43.388145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9ea008b21f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('master_worlds',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('master_worlds', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_master_worlds_name'), ['name'], unique=True)

    op.create_table('character_cards',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('instructions', sa.Text(), nullable=True),
    sa.Column('example_dialogues', sa.JSON(), nullable=True),
    sa.Column('beginning_messages', sa.JSON(), nullable=True),
    sa.Column('master_world_id', sa.String(), nullable=True),
    sa.Column('linked_lore_ids', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['master_world_id'], ['master_worlds.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('character_cards', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_character_cards_master_world_id'), ['master_world_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_character_cards_name'), ['name'], unique=False)

    op.create_table('lore_entries',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('entry_type', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('aliases', sa.JSON(), nullable=True),
    sa.Column('faction_id', sa.String(), nullable=True),
    sa.Column('master_world_id', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['faction_id'], ['lore_entries.id'], ),
    sa.ForeignKeyConstraint(['master_world_id'], ['master_worlds.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('lore_entries', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_lore_entries_entry_type'), ['entry_type'], unique=False)
        batch_op.create_index(batch_op.f('ix_lore_entries_master_world_id'), ['master_world_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_lore_entries_name'), ['name'], unique=False)

    op.create_table('user_personas',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('master_world_id', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['master_world_id'], ['master_worlds.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_personas', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_personas_master_world_id'), ['master_world_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_personas_name'), ['name'], unique=False)

    op.create_table('chat_sessions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('card_type', sa.String(length=20), nullable=True),
    sa.Column('card_id', sa.String(), nullable=False),
    sa.Column('user_persona_id', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_active_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['user_persona_id'], ['user_personas.id'], name='fk_chat_sessions_user_persona_id', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scenario_cards',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('instructions', sa.Text(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('beginning_message', sa.JSON(), nullable=True),
    sa.Column('example_dialogues', sa.JSON(), nullable=True),
    sa.Column('world_card_references', sa.JSON(), nullable=True),
    sa.Column('master_world_id', sa.String(), nullable=True),
    sa.Column('user_persona_id', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['master_world_id'], ['master_worlds.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_persona_id'], ['user_personas.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('scenario_cards', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_scenario_cards_master_world_id'), ['master_world_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_scenario_cards_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_scenario_cards_user_persona_id'), ['user_persona_id'], unique=False)

    op.create_table('user_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('llm_provider', sa.String(), nullable=True),
    sa.Column('selected_llm_model', sa.String(), nullable=True),
    sa.Column('llm_api_key', sa.String(), nullable=True),
    sa.Column('generation_prompt_template', sa.Text(), nullable=True),
    sa.Column('language', sa.String(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('top_p', sa.Float(), nullable=True),
    sa.Column('max_response_tokens', sa.Integer(), nullable=True),
    sa.Column('context_size', sa.Integer(), nullable=True),
    sa.Column('active_persona_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['active_persona_id'], ['user_personas.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chat_messages',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('chat_session_id', sa.String(), nullable=False),
    sa.Column('sender_type', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('message_metadata', sa.JSON(), nullable=True),
    sa.Column('active_persona_name', sa.String(), nullable=True),
    sa.Column('active_persona_image_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['chat_session_id'], ['chat_sessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat_messages')
    op.drop_table('user_settings')
    with op.batch_alter_table('scenario_cards', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_scenario_cards_user_persona_id'))
        batch_op.drop_index(batch_op.f('ix_scenario_cards_name'))
        batch_op.drop_index(batch_op.f('ix_scenario_cards_master_world_id'))

    op.drop_table('scenario_cards')
    op.drop_table('chat_sessions')
    with op.batch_alter_table('user_personas', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_personas_name'))
        batch_op.drop_index(batch_op.f('ix_user_personas_master_world_id'))

    op.drop_table('user_personas')
    with op.batch_alter_table('lore_entries', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_lore_entries_name'))
        batch_op.drop_index(batch_op.f('ix_lore_entries_master_world_id'))
        batch_op.drop_index(batch_op.f('ix_lore_entries_entry_type'))

    op.drop_table('lore_entries')
    with op.batch_alter_table('character_cards', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_character_cards_name'))
        batch_op.drop_index(batch_op.f('ix_character_cards_master_world_id'))

    op.drop_table('character_cards')
    with op.batch_alter_table('master_worlds', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_master_worlds_name'))

    op.drop_table('master_worlds')
    # ### end Alembic commands ###
