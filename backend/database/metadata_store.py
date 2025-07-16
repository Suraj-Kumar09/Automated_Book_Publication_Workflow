def save_review(chapter_id, comments, rating):
    with open(f"data/versions/{chapter_id}_review.json", "w") as f:
        json.dump({"comments": comments, "rating": rating}, f)
