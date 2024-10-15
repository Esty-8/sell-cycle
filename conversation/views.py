from django.shortcuts import render, get_object_or_404
from product.models import Product

from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required



def new_conversation(request, product_pk):
    product = get_object_or_404(Product, ok=product_pk)
    conversations = Conversation.objects.filter(product=product, users__in=[request.user])
    
    # Prevent the product creator from starting a conversation
    if product.created_by == request.user:
        return redirect('catalogue:index')

    # Check for existing conversations
    conversations = Conversation.objects.filter(product=product).filter(members__in=[request.user.id])

    if conversations:
        pass #redirect to conversation


    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(product=product)
            conversation.members.add(request.user)
            conversation.members.add(product.created_by)
            conversation.save()
               

            # Save the message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('product:information', pk=product_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/message.html', {
        'form': form,
        'conversation': conversation,
    })


