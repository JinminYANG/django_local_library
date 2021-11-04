from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('action_live/', views.action_live, name='action_live'),
    path('fan_page/', views.fan_page, name='fan_page'),


    path('books/', views.BookListView.as_view(), name='books'),
    # URL('books/')과 매치되는 패턴,
    # URL이 매치될 때 호출되는 view 함수(views.BookListView.as_view())
    # 이 특정 매핑에 대한 이름을 정의

    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # 꺾쇠 괄호는 캡처하는 URL의 일부를 정의하고 뷰가 캡처 된 데이터에 액세스하는 데 사용할 수있는 변수의 이름을 지정
    # '<int:pk>' 포맷화된 문자열 <Integer / Primary Key>

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    path('borrowed/', views.LoanedBooksByAllListView.as_view(), name='users-borrowed'),

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    # URL 구성은 /book/<bookinstance_id>/pk/ 형식의 URL을 views.py에서 renew_book_function이라는 함수로 리디렉션하고 BookInstance ID를 pk라는 매개 변수로 보낸다.
    # 패턴은 pk가 올바른 형식의 UUID인 경우에만 일치합니다.

    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    # views가 클래스 이므로 .as_view()를 통해 호출해야 하며,
    # 각 경우에 URL 패턴을 인식할 수 있어야 한다.
    # 기본 키값의 이름으로 pk를 사용해야 하고, 이 이름은 views 클래스에서 예상하는 매개변수 이름이다.

    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]
