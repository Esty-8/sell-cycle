from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product

from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required


@login_required
def new_conversation(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    
    conversations = Conversation.objects.filter(product=product).filter(users__in=[request.user.id])
    
    # Prevent the product creator from starting a conversation
    if product.created_by == request.user:
        return redirect('catalogue:index')

    # Check for existing conversations
    

    if conversations:
        pass #redirect to conversation


    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(product=product)
            conversation.users.add(request.user)
            conversation.users.add(product.created_by)
            conversation.save()
               

            # Save the message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('product:product_information', product_id)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/message.html', {
        'form': form,
        
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(users__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
    })


@login_required
def detail(request, pk):
    # Retrieve the conversation or raise a 404 if not found
   conversation = Conversation.objects.filter(users__in=[request.user.id]).get(pk=pk)
# Initialize the form for both GET and POST requests
   form = ConversationMessageForm(request.POST or None)  

   if request.method == 'POST' and form.is_valid():
  
    conversation_message = form.save(commit=False)
    conversation_message.conversation = conversation
    conversation_message.created_by = request.user
    conversation_message.save()


     # Redirect to the conversation detail page
    return redirect('conversation:detail', pk=pk)

    
     # Render the conversation details with the form
   return render(request, 'conversation/details.html', {
    'conversation': conversation,
    'form':form,
   })