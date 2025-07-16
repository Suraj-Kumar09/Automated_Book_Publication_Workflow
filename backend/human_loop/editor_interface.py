from fastapi import APIRouter, Body
router = APIRouter()
@router.post("/editor/finalize")
def finalize(chapter_id: str, final_text: str = Body(...)):
    mark_as_final(chapter_id, final_text)
    return {"status": "finalized"}
