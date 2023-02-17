import strawberry
from strawberry.file_uploads import Upload

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter



@strawberry.type
class ImageUploadMutation:

    @strawberry.mutation
    async def read_file(self, pk: str, file: Upload) -> str:
        print(pk) # I want this to work
        return (await file.read()).decode('utf-8')  # type: ignore

@strawberry.type
class ImageUploadQuery:

    @strawberry.field
    async def list_images(self, pk: str) -> int:
        """This function lists all images for a user"""
        return 4


image_schema = strawberry.Schema(query=ImageUploadQuery,
                                 mutation=ImageUploadMutation)


image_upload = GraphQLRouter(image_schema, graphiql=True)

app = FastAPI()
app.include_router(image_upload, prefix="/upload")

@app.get("/")
async def root():
    """ The root of the FastAPI app """
    return {"message": "Hello World"}