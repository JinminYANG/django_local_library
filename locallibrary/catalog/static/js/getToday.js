import Datepicker from './vanillajs-datepicker-master/js/Datepicker.js';
import ko from './vanillajs-datepicker-master/js/i18n/locales/ko.js'; // datepicker 한글패치
// import { today } from './vanillajs-datepicker-master/js/lib/date.js';

Object.assign(Datepicker.locales, ko); // datepicker 한글패치

class Today {
    constructor() {
        this.datepickerInput = document.querySelector('input[name="datepicker"]');
        this.datepicker = new Datepicker(this.datepickerInput, {
            // ...options
            buttonClass: 'btn',
            autohide: true,
            language: 'ko',
            container: true,
            format: 'mm월dd일(D)',
            todayHighlight: true,
            updateOnBlur: false,
            setDate: new Date(),

        });

        this.todayDate = new Date();
        this.year = this.todayDate.getFullYear();
        this.month = this.todayDate.getMonth() + 1;
        this.date = this.todayDate.getDate();
        this.day = this.todayDate.getDay();
    }

    setDefaultToday() {
        const dayToKor = new Intl.DateTimeFormat('ko-KR', { weekday: 'short' }).format(this.day);
        return this.datepickerInput.value = `${this.month}월${this.date}일(${dayToKor})`
    }

    getToday() {
        return this.datepickerInput.value;
    }

}

window.onload = () => {
    const date = new Today();
    date.setDefaultToday();

    date.datepickerInput.addEventListener('changeDate', function(e, details) { // 날짜 변경시 이벤트
        console.log(date.getToday());
    });



};