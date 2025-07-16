def writer_reward(generated_text, original_text, user_score):
    similarity = compute_similarity(generated_text, original_text)
    length_diff_penalty = abs(len(generated_text) - len(original_text)) / len(original_text)
    return 0.5 * similarity + 0.3 * user_score - 0.2 * length_diff_penalty
