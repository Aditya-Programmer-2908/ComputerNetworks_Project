from django.db import models
import uuid

class FileTransfer(models.Model):
    file = models.FileField(upload_to='uploads/')
    retrieval_code = models.CharField(max_length=50, unique=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.retrieval_code:
            self.retrieval_code = str(uuid.uuid4())[:8]  
        super().save(*args, **kwargs)


class ClipboardContent(models.Model):
    content = models.TextField() 
    retrieval_code = models.CharField(max_length=50, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.retrieval_code}: {self.content[:30]}"
    

class EncryptedFile(models.Model):
    file_name = models.CharField(max_length=255)
    encrypted_data = models.BinaryField()
    encryption_key = models.BinaryField()
    retrieval_code = models.CharField(max_length=50, unique=True)

class EncryptedClipboard(models.Model):
    encrypted_content = models.BinaryField()
    encryption_key = models.BinaryField()
    retrieval_code = models.CharField(max_length=50, unique=True)

