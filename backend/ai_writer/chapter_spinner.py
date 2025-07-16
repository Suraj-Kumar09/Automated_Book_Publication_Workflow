def spin_chapter(text, style="simplified"):
    prompt = f"Rewrite this in {style} style:\n\n{text}"
    return call_llm(prompt)  # Placeholder for your LLM API
