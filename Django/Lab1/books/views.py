from django.shortcuts import render, redirect

books = []

def book_list(request):
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        books.append({'title': title})
        return redirect('book_list')
    return render(request, 'books/book_form.html')

def book_detail(request, index):
    book = books[index]
    return render(request, 'books/book_detail.html', {'book': book})

def book_update(request, index):
    book = books[index]
    if request.method == "POST":
        title = request.POST.get('title')
        book['title'] = title
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, index):
    books.pop(index)
    return redirect('book_list')
