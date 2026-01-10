def individual_data(note):
    return {
        "id": str(note.get("_id")),
        "title": note.get("title", ""),
        "description": note.get("description", "")
    }

def all_task(notes):
    return [individual_data(note) for note in notes]

