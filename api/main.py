from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from db import UserQueries

app = FastAPI()

class category(BaseModel):
    id: int
    title: str
    canon: bool = False

class categories(BaseModel):
    categories: list[category]


@app.get("/api/categories", response_model = categories)
def categories_list(queries: UserQueries = Depends()):
    return {
        "categories": queries.get_all_categories(page=0)
    }

@app.post("/api/categories", response_model = category)
def create_item(category: category):
    return category

@app.get("/api/categoriespage={N}", response_model = categories)
def categories_page_list(queries: UserQueries = Depends(), N : int = 0):
    return {
        "categories": queries.get_all_categories(page=N)
    }

@app.put("/api/categories/{id}", response_model = category)
def category_update(id: int, titl: str, category: UserQueries = Depends()):
    return {"deleted": category.update_category(ident = id, title = titl)}
# def category_details(id: int, Category: UserQueries = Depends()):
#     # stored_category_data = categories[id]
#     # stored_category_model = category(**stored_category_data)
#     # udate_data = Category.dictxclude_unset = True)
#     # updated_category  = stored_category_model.copy(update = update_data)
#     updated_category = jsonable_encoder(Category.get_category())
#     Category.get_category()[id] = updated_category
#     return updated_category
# 
@app.delete("/api/categories/{id}", response_model = categories)
def category_delete(category: UserQueries = Depends(), id: int = 0):
    return {"categories":category.get_category(ident = id)}