from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory store
notes_db: Dict[int, dict] = {}
next_id = 1

# Data model
class Note(BaseModel):
    title: str
    content: str

# Create a note
@app.post("/notes/")
def create_note(note: Note):
    global next_id
    notes_db[next_id] = note.dict()
    notes_db[next_id]['id'] = next_id
    next_id += 1
    return notes_db[next_id - 1]

# Get all notes
@app.get("/notes/")
def get_notes():
    return list(notes_db.values())

# Get a single note by ID
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes_db[note_id]

# Update a note
@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    notes_db[note_id].update(updated_note.dict())
    return notes_db[note_id]

# Delete a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    deleted = notes_db.pop(note_id)
    return {"message": "Note deleted", "note": deleted}
