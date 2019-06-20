from django_chunk_upload.models import ChunkUpload


class MyChunkUpload(ChunkUpload):
    pass


# Override the default ChunkUpload to make the `user` field nullable
MyChunkUpload._meta.get_field('user').null = True
