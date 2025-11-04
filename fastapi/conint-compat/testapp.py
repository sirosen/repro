from fastapi import FastAPI, Query

import pydantic

import typing as t


class MyQueryModel(pydantic.BaseModel):
    who: str = "you"
    counter: pydantic.conint(ge=0, le=10) = 5


app = FastAPI()


@app.get("/")
def read_root(qargs: t.Annotated[MyQueryModel, Query()]):
    return {"Hello": qargs.who}
