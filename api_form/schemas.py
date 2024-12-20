from sqlmodel import Field, SQLModel

class LeadBase(SQLModel):
    name: str
    email: str
    phone: str


class Lead(LeadBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class LeadPublic(LeadBase):
    id: int


class LeadCreate(LeadBase):
    pass


class LeadUpdate(LeadBase):
    name: str | None = None
    email: int | None = None
    phone: str | None = None