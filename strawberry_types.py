import strawberry
from typing import List
from global_state import file_contents, lock

@strawberry.type
class FileData:
    filename: str
    content: str

@strawberry.type
class Query:
    @strawberry.field
    def files(self) -> List[FileData]:
        with lock:
            return [FileData(filename=k, content=v) for k, v in file_contents.items()]

schema = strawberry.Schema(query=Query)
