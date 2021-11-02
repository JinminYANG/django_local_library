// 막무가내 코드
// document.addEventListener("DOMContentLoaded", function() {
//     const effectsBtn = document.querySelector('#controlsEffects');
//     const predictionBtn = document.querySelector('#controlsPrediction');
//     const playerInfoBtn = document.querySelector('#controlsPlayerInfo');

//     const effectsContainer = document.querySelector('#effects');
//     const predictionContainer = document.querySelector('#prediction');
//     const playerInfoContainer = document.querySelector('#playerInfo');


//     effectsBtn.addEventListener('click', function() {
//         predictionBtn.classList.remove('active');
//         playerInfoBtn.classList.remove('active');
//         effectsBtn.classList.add('active');

//         predictionContainer.classList.remove('active');
//         playerInfoContainer.classList.remove('active');
//         effectsContainer.classList.add('active');
//     });

//     predictionBtn.addEventListener('click', function() {
//         effectsBtn.classList.remove('active');
//         playerInfoBtn.classList.remove('active');
//         predictionBtn.classList.add('active');

//         effectsContainer.classList.remove('active');
//         playerInfoContainer.classList.remove('active');
//         predictionContainer.classList.add('active');
//     });

//     playerInfoBtn.addEventListener('click', function() {
//         effectsBtn.classList.remove('active');
//         predictionBtn.classList.remove('active');
//         playerInfoBtn.classList.add('active');

//         effectsContainer.classList.remove('active');
//         predictionContainer.classList.remove('active');
//         playerInfoContainer.classList.add('active');
//     });
// });


// 어느정도 생각
Array.from(document.querySelectorAll('.controls__item')).forEach((button) => {
    button.addEventListener('click', () => {
        hideAllShadowEffect(button);
        displayShadowEffect(button);

        hideSettingItem();
        displaySettingItem(button);
    });
})

function displayShadowEffect(button) {
    return button.classList.add('active');
}

function hideAllShadowEffect(button) {
    const items = button.parentElement.children;
    Array.from(items).forEach((btn) => {
        btn.classList.remove('active');
    });

    return;
}

function displaySettingItem(button) {
    if (button.classList.contains('controls__effects')) {
        return document.querySelector('#effects').classList.add('active');
    } else if (button.classList.contains('controls__prediction')) {
        return document.querySelector('#prediction').classList.add('active');
    } else if (button.classList.contains('controls__player_info')) {
        return document.querySelector('#playerInfo').classList.add('active');
    } else {
        return;
    }
}

function hideSettingItem() {
    Array.from(document.querySelectorAll('.setting')).forEach((elem) => {
        elem.classList.remove('active');
    });

    return;
}


// 클래스???

class Setting {
    constructor(_effectsBtn, _predictionBtn, _playerInfoBtn, _effectsContainer, _predictionContainer, _playerInfoContainer) {
        this.effectsBtn = _effectsBtn;
        this.predictionBtn = _predictionBtn;
        this.playerInfoBtn = _playerInfoBtn;

        this.effectsContainer = _effectsContainer;
        this.predictionContainer = _predictionContainer;
        this.playerInfoContainer = _playerInfoContainer;
    }

    clickedButton() {

    }


}

const effectsBtn = document.querySelector('#controlsEffects');
const predictionBtn = document.querySelector('#controlsPrediction');
const playerInfoBtn = document.querySelector('#controlsPlayerInfo');

const effectsContainer = document.querySelector('#effects');
const predictionContainer = document.querySelector('#prediction');
const playerInfoContainer = document.querySelector('#playerInfo');

const setting = new Setting(effectsBtn, predictionBtn, playerInfoBtn, effectsContainer, predictionContainer, playerInfoContainer);

console.log(setting);