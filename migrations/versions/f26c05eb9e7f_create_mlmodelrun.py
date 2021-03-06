"""Create MLModelRun

Revision ID: f26c05eb9e7f
Revises: de5e17d0c54c
Create Date: 2020-11-22 03:00:08.393236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f26c05eb9e7f'
down_revision = 'de5e17d0c54c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ml_model_run',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('csv_filename', sa.String(length=256), nullable=False),
    sa.Column('ml_model_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ml_model_id'], ['ml_model.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('csv_filename')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ml_model_run')
    # ### end Alembic commands ###
