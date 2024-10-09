from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

def getCollections():
    qdrant_client = QdrantClient(
    url="https://3440a36e-8a0c-4f1a-8a24-a6afa7136eca.europe-west3-0.gcp.cloud.qdrant.io:6333", 
    api_key="vJDSWadeF0guuVKUtJr77Idy92H-Y2En0Or0kCo8ss2gQnO-kXgFzQ",)
    return qdrant_client.get_collections()

def createCollection(collectionName):
    qdrant_client = QdrantClient(
    url="https://3440a36e-8a0c-4f1a-8a24-a6afa7136eca.europe-west3-0.gcp.cloud.qdrant.io:6333", 
    api_key="vJDSWadeF0guuVKUtJr77Idy92H-Y2En0Or0kCo8ss2gQnO-kXgFzQ",)
    response =qdrant_client.create_collection(
        collection_name=collectionName,
        vectors_config=VectorParams(size=100, distance=Distance.COSINE) )
    print(response)

    
print(getCollections())
#Adding New Collection with name JusBot
createCollection("jusBot")
print(getCollections())