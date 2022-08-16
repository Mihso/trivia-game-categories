from tkinter import N
from typing import Union

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from db import UserQueries

app = FastAPI()

class category(BaseModel):
    id: int
    title: str
    canon: bool

class categories(BaseModel):
    categories: list[category]


@app.get("/api/categories", response_model = categories)
def categories_list(queries: UserQueries = Depends()):
    return {
        "categories": queries.get_all_categories(page=0)
    }

@app.post("/api/categories")
def create_item(category: category):
    return category

@app.get("/api/categoriespage={N}", response_model = categories)
def categories_page_list(queries: UserQueries = Depends(), N : int = 0):
    return {
        "categories": queries.get_all_categories(page=N)
    }