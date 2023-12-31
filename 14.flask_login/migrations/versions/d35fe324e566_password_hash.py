"""password_hash

Revision ID: d35fe324e566
Revises: cd1d781ded0e
Create Date: 2023-08-01 11:13:25.035224

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from app import User
from werkzeug.security import generate_password_hash, check_password_hash

# revision identifiers, used by Alembic.
revision = 'd35fe324e566'
down_revision = 'cd1d781ded0e'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=120), nullable=True))

    # DB 연결
    bind = op.get_bind()
    session = Session(bind=bind)

    # 데이터 가져오기
    users = session.query(User).all()

    # 데이터 변환 과정
    for user in users:
        user.password_hash = generate_password_hash(user.password)
        print(f'{user}, {user.username}, {user.password} -> {user.password_hash}')

    session.commit()
    session.close()

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash', nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
