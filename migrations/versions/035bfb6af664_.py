"""empty message

Revision ID: 035bfb6af664
Revises: 0cf78c319ccb
Create Date: 2018-07-24 18:20:36.954841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '035bfb6af664'
down_revision = '0cf78c319ccb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'person', ['email_address'])
    op.create_unique_constraint(None, 'students', ['student_id'])
    op.create_unique_constraint(None, 'subjects', ['subject_id'])
    op.create_unique_constraint(None, 'teachers', ['staff_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teachers', type_='unique')
    op.drop_constraint(None, 'subjects', type_='unique')
    op.drop_constraint(None, 'students', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    # ### end Alembic commands ###