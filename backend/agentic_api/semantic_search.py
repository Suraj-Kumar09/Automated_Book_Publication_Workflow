def search_similar(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results['documents']
