def compute_reward(text, feedback_score, sim_score):
    return 0.5 * sim_score + 0.5 * feedback_score
