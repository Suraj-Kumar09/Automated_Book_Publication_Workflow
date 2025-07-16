def review_chapter(text):
    prompt = f"Review this rewritten chapter for clarity, flow, and tone:\n\n{text}\nGive score out of 10."
    return call_llm(prompt)  # returns text + score
