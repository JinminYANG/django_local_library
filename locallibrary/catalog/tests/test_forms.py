import datetime

from django.test import TestCase
from django.utils import timezone

from catalog.forms import RenewBookForm

# renewing books
class RenewBookFormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label is None or form.fields['renewal_date'].label == 'renewal date')

    def test_renew_form_date_field_help_text(self):
        form = RenewBookForm()
        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')

    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = timezone.localtime() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

# 처음 두 함수는 필드의 레이블과 help_text가 예상대로인지 테스트합니다.
# 필드 사전(예: form.fields['renew_date'])을 사용하여 필드에 액세스해야 합니다.
# 또한 레이블 값이 없음인지 테스트해야 합니다.
# Django가 올바른 레이블을 렌더링하더라도 값이 명시적으로 설정되지 않으면 없음을 반환합니다.

# 나머지 기능은 해당 양식이 허용 범위 바로 안에 있는 갱신 날짜에 유효하고 범위를 벗어난 값에 유효하지 않은지 테스트합니다.
# datetime.timedelta()를 사용하여 현재 날짜(datetime.date.today())를 기준으로 테스트 날짜 값을 구성하는 방법을
# 기록합니다(이 경우 일 또는 주를 지정합니다).
# 그런 다음 양식을 작성하여 데이터를 전달한 후 유효한지 테스트합니다.
