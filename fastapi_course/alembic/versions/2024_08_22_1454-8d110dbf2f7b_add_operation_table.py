"""add operation table

Revision ID: 8d110dbf2f7b
Revises: 394c2e56b110
Create Date: 2024-08-22 14:54:33.047045

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8d110dbf2f7b"
down_revision: Union[str, None] = "394c2e56b110"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "operation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.String(), nullable=False),
        sa.Column("figi", sa.String(), nullable=False),
        sa.Column("instrument_type", sa.String(), nullable=False),
        sa.Column("date", sa.TIMESTAMP(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("operation")
    # ### end Alembic commands ###
