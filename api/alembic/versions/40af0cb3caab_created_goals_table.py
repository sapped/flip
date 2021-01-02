"""created goals table

Revision ID: 40af0cb3caab
Revises: 5b72d1cc957f
Create Date: 2021-01-01 23:08:49.653591

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '40af0cb3caab'
down_revision = '5b72d1cc957f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('has_amount', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_goals_id'), 'goals', ['id'], unique=False)
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('tracked', sa.Boolean(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entries_id'), 'entries', ['id'], unique=False)
    op.drop_index('ix_tracker_id', table_name='tracker')
    op.drop_table('tracker')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tracker',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('crossfit', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('gowod', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('yoga', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('weight', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('calories', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tracker_pkey')
    )
    op.create_index('ix_tracker_id', 'tracker', ['id'], unique=False)
    op.drop_index(op.f('ix_entries_id'), table_name='entries')
    op.drop_table('entries')
    op.drop_index(op.f('ix_goals_id'), table_name='goals')
    op.drop_table('goals')
    # ### end Alembic commands ###