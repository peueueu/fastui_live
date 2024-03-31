from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastui import FastUI, prebuilt_html, components as c
from fastui import AnyComponent
from fastui import events
from fastui.components.display import DisplayLookup
from pydantic import BaseModel

app = FastAPI()
form_string = Annotated[str, Form()]
user_form_id = Annotated[int, Form()]


class User(BaseModel):
    id: int
    name: str
    phone: str


database: list[User] = [User(id=1, name="Anderson da Meiota", phone="(66) 9 6666-6666")]

NAVBAR = c.Navbar(
    title="FastUI APP",
    title_event=events.GoToEvent(url="/"),
    start_links=[
        c.Link(
            on_click=events.GoToEvent(url="/register"),
            components=[c.Text(text="Register")],
        ),
    ],
)


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def api() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                NAVBAR,
                c.Table(
                    data=database,
                    data_model=User,
                    columns=[
                        DisplayLookup(
                            field="id", on_click=events.GoToEvent(url="/details/{id}")
                        ),
                        DisplayLookup(field="name"),
                        DisplayLookup(field="phone"),
                    ],
                ),
                c.Button(text="Add User", on_click=events.GoToEvent(url="/register")),
            ]
        )
    ]


@app.get("/api/register", response_model=FastUI, response_model_exclude_none=True)
def register_view() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                NAVBAR,
                c.Form(
                    submit_url="/register",
                    form_fields=[
                        c.forms.FormFieldInput(name="name", title="Name:"),
                        c.forms.FormFieldInput(name="phone", title="Phone:"),
                    ],
                ),
            ]
        )
    ]


@app.get(
    "/api/details/{user_id}", response_model=FastUI, response_model_exclude_none=True
)
def details(user_id: int) -> list[AnyComponent]:
    user = database[user_id - 1]
    return [
        c.Page(
            components=[
                NAVBAR,
                c.Heading(text=user.name, level=1),
                c.Details(data=user),
                c.Button(
                    text="Edit",
                    named_style="primary",
                    on_click=events.GoToEvent(url=f"/edit/{user.id}"),
                ),
                c.Button(
                    text="Go back",
                    on_click=events.BackEvent(),
                    named_style="secondary",
                ),
                c.Button(
                    text="Delete",
                    on_click=events.GoToEvent(url=f"/delete/{user.id}"),
                    named_style="warning",
                ),
            ]
        )
    ]


@app.get("/api/edit/{user_id}", response_model=FastUI, response_model_exclude_none=True)
def edit(user_id: int) -> list[AnyComponent]:
    user = database[user_id - 1]
    return [
        c.Page(
            components=[
                NAVBAR,
                c.Heading(text="Editar", level=1),
                c.Form(
                    submit_url="/edit",
                    form_fields=[
                        c.forms.FormFieldInput(
                            name="id", title="ID:", initial=user.id, locked=True
                        ),
                        c.forms.FormFieldInput(
                            name="name", title="Name:", initial=user.name
                        ),
                        c.forms.FormFieldInput(
                            name="phone", title="Phone:", initial=user.phone
                        ),
                    ],
                ),
            ]
        )
    ]


@app.get(
    "/api/delete/{user_id}", response_model=FastUI, response_model_exclude_none=True
)
def delete(user_id: int) -> list[AnyComponent]:
    del database[user_id - 1]
    return [c.FireEvent(event=events.GoToEvent(url="/"))]


@app.post("/register")
def register(name: form_string, phone: form_string) -> list[AnyComponent]:
    database.append(User(id=len(database) + 1, name=name, phone=phone))
    return [c.FireEvent(event=events.GoToEvent(url="/"))]


@app.post("/edit")
def edit(id: user_form_id, name: form_string, phone: form_string):
    database[id - 1] = User(id=id, name=name, phone=phone)
    return [c.FireEvent(event=events.GoToEvent(url="/"))]


@app.get("/{path:path}")
def home():
    return HTMLResponse(prebuilt_html(title="FastUI APP"))
