from django.shortcuts import render
from django.conf import settings
from .forms import TextInputForm
from datetime import datetime
import os


def index(request):
    """Display form and history"""
    form = TextInputForm()
    history = []
    
    # Handle form submission
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text_input = form.cleaned_data['text_input']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Ensure logs directory exists
            log_file = settings.EX02_LOG_FILE
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            
            # Write to log file
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {text_input}\n")
            
            # Clear form for new input
            form = TextInputForm()
    
    # Read history from log file
    log_file = settings.EX02_LOG_FILE
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    # Parse timestamp and text from log line
                    if line.startswith('[') and ']' in line:
                        timestamp_end = line.index(']')
                        timestamp = line[1:timestamp_end]
                        text = line[timestamp_end + 2:].strip()
                        history.append({
                            'timestamp': timestamp,
                            'text': text
                        })
    
    context = {
        'form': form,
        'history': history
    }
    
    return render(request, 'indexx.html', context)
