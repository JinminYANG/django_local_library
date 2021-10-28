from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic    # 존재하는 generic view 함수를 상속받아 view 함수를 구현
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# 우리의 모든 뷰들 안에서 데이터에 접근하는 데 사용할 모델 클래스들을 포함(import)
def index(request):
    """View function for home page of site."""
    # 일부 주요 개체의 개수 생성
    # 모델 클래스들에서 objects.all() 속성을 사용하는 레코드들의 개수를 가져옵니다.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genre = Genre.objects.filter(name='fiction')
    books_genre_title = Book.objects.filter(genre='1').values('title')

    # 사용 가능한 책(상태 = 'a')
    # 상태 필드에서 'a'(Available) 값을 가지고 있는 BookInstance 객체들의 목록도 가져옵니다.
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # 'all()'은 기본적으로 내포되어 있습니다.
    num_authors = Author.objects.count()

    # 세션 변수에서 계산한 이 보기에 대한 방문 횟수입니다.
    num_visits = request.session.get('num_visits', 0)
    # 'num_visits' 세션 키 값을 가져와 이전에 설정하지 않은 경우 값을 0으로 설정한다.
    request.session['num_visits'] = num_visits + 1
    # 요청이 수신될 때마다 값을 증가시키고 세션에 다시 저장한다. (다음 번에 사용자가 페이지를 방문할 때)

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'books_genre_title': books_genre_title,
        'num_visits': num_visits,   # 'num_visits' 변수는 템플릿에 전달된다
    }

    # 컨텍스트 변수의 데이터로 HTML 템플릿 index.html을 렌더링합니다.
    # HTML 페이지를 생성하고 이 페이지를 응답으로서 반환하기 위해 render() 함수를 호출합니다.
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    # 모든 책에 대한 데이터베이스 쿼리를 만들어서 render() 함수를 불러 특정 템플릿에 리스트를 보낸다
    # 이미 존재하는 뷰로부터 상속받아온 클래스 => class-based generic list view (ListView)
    # generic view가 이미 우리가 필요한 대부분의 기능성을 실행하면서 동시에 Django best-practice
    # 코드의 양과 반복을 줄이고 유지보수에 좋은 리스트 뷰를 만들 수 있다.
    model = Book
    paginate_by = 5
    # 장고는 pagination에 대한 지원을 하고 있다. 제네릭 클래스 기반 list view에 내장되어 있다.

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    # 로그인 필수 사용자만 보기를 호출할 수 있도록 LoginRequiredMixin에서 가져오소 파생한다.
    # 뷰와 템플릿이 다른 BookInstance 레코드의 몇 가지 다른 목록이 나타날 수 있으므로 기본값을 사용하지 않고 template_name을 선언하도록 선택할 것이다.
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    # 현재 사용자의 BookInstance 개체로만 쿼리를 제한하기 위해 위와 같이 get_queryset()을 다시 구현한다
    # "o"는 "대출 중"에 대한 저장된 코드이며 가장 오래된 항목이 먼저 표시되도록 만기일까지 주문한다.
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedBooksByAllListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # POST 요청인 경우 양식 데이터를 처리합니다.
    if request.method == 'POST':

        # 양식 인스턴스를 만들고 요청(바인딩)의 데이터로 채웁니다:
        form = RenewBookForm(request.POST)

        # 양식이 유효한지 확인합니다.
        if form.is_valid():
            # 필요에 따라 데이터를 form_cleaned_data로 처리하다
            # (여기서는 model due_back 필드에 기록하기만 하면 됩니다.)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('users-borrowed') )

    # GET(또는 다른 방법)인 경우 기본 양식을 만듭니다.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre']

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'  # Not recommended (potential security issue if more fields added)

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')


def action_live(request):
    # 세션 변수에서 계산한 이 보기에 대한 방문 횟수입니다.
    num_visits = request.session.get('num_visits', 0)
    # 'num_visits' 세션 키 값을 가져와 이전에 설정하지 않은 경우 값을 0으로 설정한다.
    request.session['num_visits'] = num_visits + 1
    # 요청이 수신될 때마다 값을 증가시키고 세션에 다시 저장한다. (다음 번에 사용자가 페이지를 방문할 때)

    context = {
        'num_visits': num_visits,   # 'num_visits' 변수는 템플릿에 전달된다
    }

    # 컨텍스트 변수의 데이터로 HTML 템플릿 index.html을 렌더링합니다.
    # HTML 페이지를 생성하고 이 페이지를 응답으로서 반환하기 위해 render() 함수를 호출합니다.
    return render(request, 'action_live.html', context=context)