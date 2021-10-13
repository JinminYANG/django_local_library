from django.test import TestCase
from catalog.models import Author


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    # 클래스 레벨 설정을 위한 테스트 실행 시작 시 한번 호출된다.
    # 테스트 방법에서 수저아거나 변경하지 않을 개체를 만드는 데 사용된다.

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    # 테스트에 의해 수정될 수 있는 객체를 설정하기 위해 모든 테스트 함수 앞에 호출된다.
    # 모든 테스트 함수는 이러한 객체의 'fresh' 버전을 얻게 된다.

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
    # Assert 함수는 사용하는 여러가지 테스트
    # unittest에서 제공하는 표준 주장
    # 프레임워크에는 다른 표준 주장과 특정 템플릿이 사용되었는지 테스트하기 위해 view가 디리렉션되는지 테스트하기 위한 Django의 주장도 있다.


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
    # author.first_name.verbose_name을 사용하여 직접 verbose_name을 가져올 수 없습니다.
    # author.first_name은 문자열(속성에 액세스하는 데 사용할 수 있는 first_name 개체의 핸들이 아닙니다.
    # (대신 작성자의 _meta 특성을 사용하여 필드의 인스턴스를 가져오고 이를 사용하여 추가 정보를 쿼리해야 합니다.)
    # assertTrue(field_label == '이름') 대신 assertEqual(field_label, '이름')을 사용하도록 선택했습니다.
    # 그 이유는 테스트가 실패할 경우 전자에 대한 출력이 레이블이 실제로 무엇이었는지 알려주기 때문에 문제를 디버깅하는 것이 조금 더 쉬워지기 때문입니다.
