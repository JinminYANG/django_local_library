import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']    # 데이터를 가져옴

        # 날짜가 과거가 아닌지 확인합니다.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
            # 유효하지 않은 값이 입력될 경우 양식에 표시할 오류 텍스트를 지정하는 ValidationError가 발생한다

        # 날짜가 허용 범위(+오늘부터 4주) 내에 있는지 확인합니다.
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
            # 유효하지 않은 값이 입력될 경우 양식에 표시할 오류 텍스트를 지정하는 ValidationError가 발생한다

        # 변경 여부에 관계없이 이 데이터를 반환
        return data
