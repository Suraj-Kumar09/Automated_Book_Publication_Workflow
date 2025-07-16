import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection("chapter_versions")

def store_version(chapter_id, text, meta):
    collection.add(documents=[text], ids=[chapter_id], metadatas=meta)
