"""first commit

Revision ID: e74329689b23
Revises: 
Create Date: 2021-01-03 16:12:23.163633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e74329689b23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('has_amount', sa.Boolean(), nullable=False),
    sa.Column('date_created', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('goal')
    )
    op.create_index(op.f('ix_goals_id'), 'goals', ['id'], unique=False)
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Float(), nullable=False),
    sa.Column('tracked', sa.Boolean(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entries_id'), 'entries', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entries_id'), table_name='entries')
    op.drop_table('entries')
    op.drop_index(op.f('ix_goals_id'), table_name='goals')
    op.drop_table('goals')
    # ### end Alembic commands ###