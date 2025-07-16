def compute_scrape_reward(content):
    lines = content.strip().split('\n')
    length_score = min(len(lines) / 100, 1.0)  # reward for length
    completeness_score = 1.0 if "Chapter" in content else 0.5
    return 0.6 * length_score + 0.4 * completeness_score
