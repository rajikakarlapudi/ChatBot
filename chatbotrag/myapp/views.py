import openai
import os
import json
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

# Set your OpenAI API key
openai.api_key = 'add in furture'


# Path to the metadata file
METADATA_FILE = 'uploads/metadata.json'

def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        dataset_name = request.POST['dataset_name']
        domain = request.POST['domain']
        uploaded_files = request.FILES.getlist('files')
        fs = FileSystemStorage(location='uploads/')
        
        # Save the files and metadata
        for uploaded_file in uploaded_files:
            fs.save(uploaded_file.name, uploaded_file)
        
        # Load existing metadata
        if os.path.exists(METADATA_FILE):
            with open(METADATA_FILE, 'r') as f:
                metadata = json.load(f)
        else:
            metadata = []
        
        # Add new metadata
        metadata.append({
            'dataset_name': dataset_name,
            'domain': domain,
            'files': [uploaded_file.name for uploaded_file in uploaded_files]
        })
        
        # Save metadata
        with open(METADATA_FILE, 'w') as f:
            json.dump(metadata, f, indent=4)
        
        return redirect('success')
    
    return render(request, 'upload.html')

def success(request):
    return render(request, 'success.html')

def list_files(request):
    files = get_uploaded_files()
    return render(request, 'list_files.html', {'datasets': files})

def chatbot(request):
    if request.method == 'POST':
        user_query = request.POST['user_query']
        selected_files = request.POST.getlist('files')
        use_files_context = 'use_files' in request.POST
        response = query_openai(user_query, selected_files, use_files_context)
        return render(request, 'chatbot.html', {'response': response, 'uploaded_files': get_uploaded_files()})
    return render(request, 'chatbot.html', {'uploaded_files': get_uploaded_files()})

def get_uploaded_files():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return []

def query_openai(user_query, selected_files, use_files_context):
    context = ""
    if use_files_context:
        files_content = []
        uploads_dir = 'C:\\Users\\RAJIKAKARLAPUDI\\myproject\\uploads'
        for file_name in selected_files:
            file_path = os.path.join(uploads_dir, file_name)
            try:
                with open(file_path, 'r') as file:
                    files_content.append(file.read())
            except Exception as e:
                files_content.append(f"Error reading {file_name}: {str(e)}")
        context = "\n\n".join(files_content)
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_query}
    ]
    
    if context:
        messages.append({"role": "system", "content": "Consider the following context:\n" + context})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        return f"Error querying OpenAI: {str(e)}"
