from fastapi import APIRouter, Body
router = APIRouter()
@router.post("/writer/submit")
def writer_submit(chapter_id: str, text: str = Body(...)):
    # Save writer-edited version
    save_to_db(chapter_id, text, role="writer")
    return {"status": "saved"}
