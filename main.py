from fastapi import FastAPI, APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse  
from bson import ObjectId
from config.configuration import collection

app = FastAPI()
router = APIRouter()

app.mount("/static", StaticFiles(directory="static", check_dir=True), name="static")
templates = Jinja2Templates(directory="templates")

# HOME
@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": []}
    )

# ADD NOTE
@router.post("/add-note")
async def add_note(title: str = Form(...), description: str = Form(...)):
    collection.insert_one({
        "title": title,
        "description": description,
        "is_deleted": False
    })
    return RedirectResponse("/notes", status_code=303)

# SHOW ALL
@router.get("/notes")
async def show_notes(request: Request):
    notes = collection.find({"is_deleted": {"$ne": True}})
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": list(notes)}
    )

# SEARCH
@router.get("/search")
async def search(request: Request, query: str):
    notes = collection.find({
        "title": {"$regex": query, "$options": "i"},
        "is_deleted": {"$ne": True}
    })
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": list(notes)}
    )

# DELETE (POST, NOT DELETE)
@router.post("/delete")
async def delete(note_id: str = Form(...)):
    collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {"is_deleted": True}}
    )
    return RedirectResponse("/notes", status_code=303)

# EDIT (LOAD DATA)
@router.get("/edit")
async def edit(request: Request, note_id: str):
    note = collection.find_one({"_id": ObjectId(note_id),"is_deleted": {"$ne": True}})
    if not note:
        return RedirectResponse("/notes", status_code=303)
    
    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "note": note}
    )

# UPDATE
@router.post("/update")
async def update(
    note_id: str = Form(...),
    title: str = Form(...),
    description: str = Form(...)
):
    collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {"title": title, "description": description}}
    )
    return RedirectResponse("/notes", status_code=303)

app.include_router(router)
