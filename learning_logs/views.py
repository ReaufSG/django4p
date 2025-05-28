from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
def topics(request):
    """Show all topics."""
    return render(request, 'learning_logs/topics.html')
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    return render(request, 'learning_logs/topic.html', {'topic_id': topic_id})
def new_topic(request):
    """Add a new topic."""
    return render(request, 'learning_logs/new_topic.html')
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    return render(request, 'learning_logs/new_entry.html', {'topic_id': topic_id})
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    return render(request, 'learning_logs/edit_entry.html', {'entry_id': entry_id})
