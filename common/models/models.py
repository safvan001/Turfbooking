import uuid
from django.db import models

COMMON_CHAR_FIELD_MAX_LENGTH = 512
COMMON_NULLABLE_FIELD_CONFIG = { 
    "default": None,
    "null": True,
}
COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG = { 
    **COMMON_NULLABLE_FIELD_CONFIG,
    "blank": True,
}

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract=True