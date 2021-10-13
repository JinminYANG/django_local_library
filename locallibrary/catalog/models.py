from django.db import models

from django.urls import reverse
# URL 패턴을 반대로 하여 URL을 생성하는 데 사용

import uuid # Required for unique book instances

from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Model 클래스에서 파생된 모델을 정의하는 일반적인 클래스입니다.

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # my_field_name 라는 하나의 필드
    # models.CharField 타입, 이 필드가 영숫자(alphanumeric) 문자열을 포함한다는 뜻
    # 필드 타입들은 특정한 클래스들을 사용하여 등록되며, HTML 양식(form)에서 값을 수신할 때 사용할 유효성 검증 기준과 함께 데이터베이스에 데이터를 저장하는데 사용되는 레코드의 타입을 결정한다.
    # 필드 타입은 필드가 어떻게 저장되고 사용될지 지정하는 인수를 사용할 수 있다.
    # max_length=20 : 이 필드 값의 최대 길이는 20자임을 알립니다.
    # help_text='Enter field documentation' : 이 값이 HTML 양식(form)에서 사용자들에게 입력될 때 어떤 값을 입력해야 하는지 사용자들에게 알려주기 위해 보여주는 텍스트 라벨을 제공한다.
    # 필드 이름은 쿼리 및 템플릿에서 이를 참조하는데 쓰인다.
    # 필드는 또한 인수로 지정된 라벨을 가지고 있거나, 또는 필드 변수 이름의 첫자를 대문자로 바꾸고 밑줄을 공백으로 바꿔서 기본 라벨을 추정할 수 있다.
    #   ex) my_field_name 은 Myfieldname을 기본 라벨로 가지고 있다.
    # 필드가 선언된 순서는 모델이 폼에서 렌더링 된다면 기본 순서에 영향을 미치지만, 이것은 재정렬될 수 있다.
    ...

    # MetaData
    class Meta:
        ordering = ['-my_field_name']
    # class Meta를 선언하여 모델에 대한 모델-레벨의 메타데이터를 선언할 수 있다.
    # 메타 데이터의 가장 유용한 기능들 중 하나는 모델 타입을 쿼리할 때 반환되는 기본 레코드 순서를 제어하는 것이다.
    # 이렇게 하려면 위와 같이 필드 이름 목록의 일치 순서를 ordering 속성에 지정해야 한다.
    # 순서는 필드의 타입에 따라 달라질 것이다.
    # 위와 같이 반대로 정렬하고 싶다면 -(기호)를 필드 이름 앞에 접두사로 붙이면 된다.
    # ex) 아래와 같이 책들을 정렬하려고 한다면, ordering = ['title', '-pubdate']
    # 다른 일반적인 속성은 verbose_name = 'BetterName'
    # 여러가지 메타데이터 옵션들은 모델에 무슨 데이터베이스를 사용해야만 하는가 그리고 데이터가 어떻게 저장되는가를 제어한다

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        # MyModelName의 특정 인스턴스에 액세스하기 위한 URL을 반환합니다.
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        # 문자열 리턴을 위한 필수 메소드 (클래스 하나당 필수)
        """String for representing the MyModelName object (in Admin site etc.)."""
        # MyModelName 개체를 나타내는 문자열(관리 사이트 등에서)
        return self.field_name

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# class Language(models.Model):
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # 책에는 한 명의 저자만 있을 수 있지만 저자는 여러 책을 가질 수 있으므로 외래 키를 사용합니다.
    # 작성자는 아직 파일에 선언되지 않았기 때문에 객체가 아닌 문자열로 작성합니다.

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # 장르는 많은 책을 포함할 수 있기 때문에 ManyToManyField를 사용합니다. 책은 많은 장르를 다룰 수 있습니다.
    # 장르 클래스는 이미 정의되어 있으므로 위의 개체를 지정할 수 있습니다.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    # language = models.ManyToManyField(Language)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'



class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    # 비교하기 전에 먼저 due_back이 비어있는지 확인한다.
    # due_back 필드가 비어 있으면 Django가 페이지를 표시하는 대신 오류를 발생시킨다.
    # 빈 값은 비교할 수 없다.

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'




