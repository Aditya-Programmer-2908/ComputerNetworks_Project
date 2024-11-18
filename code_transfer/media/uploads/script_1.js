async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a file.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();
        document.getElementById('uploadStatus').innerText = result.message;
        fetchFileList();
    } catch (error) {
        console.error('Error uploading file:', error);
    }
}

async function fetchFileList() {
    try {
        const response = await fetch('/files');
        const files = await response.json();
        const fileList = document.getElementById('fileList');
        fileList.innerHTML = '';
        files.forEach(file => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<a href="/download/${file}" target="_blank">${file}</a>`;
            fileList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching file list:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchFileList);
