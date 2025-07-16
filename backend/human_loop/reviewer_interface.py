from fastapi import APIRouter, Body
router = APIRouter()
@router.post("/reviewer/submit")
def reviewer_submit(chapter_id: str, comments: str = Body(...), rating: float = Body(...)):
    # Save reviewer feedback
    save_review(chapter_id, comments, rating)
    return {"status": "review saved"}
