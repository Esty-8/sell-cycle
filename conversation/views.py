from django.shortcuts import render, get_object_or_404
from product.models import Product
from .models import Conversation
from .forms import ConversationMessageForm

# Create your views here.
def new_conversation(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

 # Prevent the product creator from starting a conversation
    if product.created_by == request.user:
        return redirect('catalogue:index')

# Check for existing conversations
    conversations = Conversation.objects.filter(product=product).filter(users__in=[request.user.id])

    if conversations:
        pass #redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_new = Conversation.objects.create(product=product)
            conversation_new.users.add(request.user)
            conversation_new.users.add(product.created_by)
            conversation_new.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation_new = conversation_new
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('product/information', pk=product_pk)
    else: 
        form = ConversationMessageForm()

    return render (request, 'conversation/message.html', {
        'form': form,
    })

            
