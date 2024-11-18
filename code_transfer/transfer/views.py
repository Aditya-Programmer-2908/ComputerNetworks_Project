from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FileTransfer
from .forms import FileUploadForm


import random
import string
from .models import EncryptedClipboard



from django.http import HttpResponse
from .models import ClipboardContent
from .utils.encryption import decrypt_data

from django.shortcuts import render
from django.http import HttpResponse
from .models import EncryptedClipboard
from .utils.encryption import decrypt_data
import os

import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import EncryptedClipboard
from .utils.encryption import decrypt_data 



def retrieve_clipboard(request):
    if request.method == 'POST':
        retrieval_code = request.POST.get('retrieval_code')  
        if retrieval_code:
            try:
                clipboard = ClipboardContent.objects.get(retrieval_code=retrieval_code)
                
                return render(request, 'retrieve_clipboard.html', {'content': clipboard.content})
            
            except ClipboardContent.DoesNotExist:
                return HttpResponse("Invalid retrieval code.", status=404)

            except Exception as e:
                return HttpResponse(f"Error retrieving clipboard content: {str(e)}", status=500)

    return render(request, 'retrieve_clipboard.html')  





"""def paste_clipboard(request):
    if request.method == "POST":
        clipboard_text = request.POST.get('clipboard_text', '')
        if clipboard_text:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            ClipboardContent.objects.create(content=clipboard_text, retrieval_code=code)
            return render(request, 'clipboard_success.html', {'code': code})
    return render(request, 'paste_clipboard.html')"""


from django.shortcuts import render, redirect
from .models import EncryptedFile
from .utils.encryption import generate_key, encrypt_data
import os

import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import EncryptedFile
from .utils.encryption import encrypt_data, generate_key  # Make sure these functions are implemented correctly

def upload_file(request):
    if request.method == "POST":
        if 'file' not in request.FILES:
            return HttpResponse("No file uploaded.", status=400)

        file = request.FILES['file']

        if file.size == 0:
            return HttpResponse("Uploaded file is empty.", status=400)

        try:
            file_data = file.read()

            encryption_key = generate_key()

            encrypted_data = encrypt_data(file_data, encryption_key)

            retrieval_code = os.urandom(16).hex()

            EncryptedFile.objects.create(
                file_name=file.name,
                encrypted_data=encrypted_data,
                encryption_key=encryption_key,
                retrieval_code=retrieval_code
            )

            file_transfer = FileTransfer.objects.create(
            file=file,  
            retrieval_code=retrieval_code
            )

            return render(request, 'upload_success.html', {'code': retrieval_code})

        except Exception as e:
            return HttpResponse(f"An error occurred while uploading the file: {str(e)}", status=500)

    return render(request, 'upload_file.html')

from .models import EncryptedClipboard

from django.shortcuts import render
from .models import EncryptedClipboard, ClipboardContent
import os

def upload_clipboard(request):
    if request.method == "POST":
        clipboard_content = request.POST.get('clipboard_content')

        if not clipboard_content:
            return render(request, 'paste_clipboard.html', {'error': 'Clipboard content cannot be empty.'})

        try:
            retrieval_code = os.urandom(16).hex()

            ClipboardContent.objects.create(
                content=clipboard_content,
                retrieval_code=retrieval_code
            )

            encryption_key = generate_key()

            encrypted_content = encrypt_data(clipboard_content.encode(), encryption_key)

            EncryptedClipboard.objects.create(
                encrypted_content=encrypted_content,
                encryption_key=encryption_key,
                retrieval_code=retrieval_code
            )

            return render(request, 'upload_success.html', {'code': retrieval_code})

        except Exception as e:
            return render(request, 'paste_clipboard.html', {'error': f"An error occurred: {str(e)}"})

    return render(request, 'paste_clipboard.html')



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import base64
from cryptography.fernet import Fernet
import os


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FileTransfer

def retrieve_file(request):
    if request.method == 'POST':
        code = request.POST.get('retrieval_code')

        if not code:
            return render(request, 'retrieve_file.html', {'error': 'Retrieval code is required.'})

        try:
            file_transfer = get_object_or_404(FileTransfer, retrieval_code=code)

            response = HttpResponse(file_transfer.file, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file_transfer.file.name.split("/")[-1]}"'
            return response

        except Exception as e:
            return render(request, 'retrieve_file.html', {'error': f'Error retrieving file: {str(e)}'})

    return render(request, 'retrieve_file.html')



def home(request):
    return render(request,'index.html')

def sender(request):
    return render(request, 'sender.html')

def receiver_options(request):
    return render(request, 'receiver_options.html')

from decouple import config

encryption_key = config('ENCRYPTION_KEY')
