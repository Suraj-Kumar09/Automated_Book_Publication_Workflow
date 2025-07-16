def rank_versions(versions):
    return sorted(versions, key=lambda v: v['reward'], reverse=True)
