from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookstoreModel

# Create your views here.
def home(request):
    return render(request,'store_book.html')

def store_book(request):
    if request.method == 'POST':
       book = BookStoreForm(request.POST)
       if book.is_valid():
          book.save() 
          print(book.cleaned_data)
          return redirect(Show_book)
          
         
    else:    
         book=BookStoreForm()
    return render (request,'store_book.html',{'form':book})


def Show_book(request):
    book = BookstoreModel.objects.all()
    print(book)
    return render(request,'show.html',{'data':book})
    
    
def edit_book(request, id):
    book = BookstoreModel.objects.get(pk = id)
    form =BookStoreForm(instance=book) 
    if request.method == 'POST':
       form = BookStoreForm(request.POST,instance=book)
       if form.is_valid():
          form.save() 
          return redirect('Show_book')
    
        
    return render (request,'store_book.html',{'form':form})

    
def delete_book(request, id):
    book = BookstoreModel.objects.get(pk = id).delete()
    return redirect('Show_book')

