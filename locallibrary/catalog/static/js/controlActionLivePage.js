// side setting Control
const sideSettingControlBtns = document.querySelectorAll('.controls__item');
Array.from(sideSettingControlBtns).forEach((button) => {
    button.addEventListener('click', () => {
        hideAllShadowEffect(button);
        displayShadowEffect(button);

        hideSettingItem();
        displaySettingItem(button);
    });
});

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

// LiveChatRoom control
const liveChatRoomControlBtn = document.querySelector(".chatting__header__toggle");

liveChatRoomControlBtn.addEventListener("click", () => {
    toggleBtn(liveChatRoomControlBtn);
});

function toggleBtn(button) {
    if (button.classList.contains("down")) {
        button.classList.remove("down");
        button.classList.add("up");
        return;
    } else {
        button.classList.remove("up");
        button.classList.add("down");
        return;
    }
}

// streamingBottomItem control
const streamingBottomItem = document.querySelectorAll(".streaming__bottom__item");
Array.from(streamingBottomItem).forEach((button) => {
    button.addEventListener('click', () => {
        toggleActive(button);
    });
});

function toggleActive(button) {
    if (button.classList.contains("active")) {
        return button.classList.remove("active");
    } else {
        return button.classList.add("active");
    }
}

const statsBtnItem = document.querySelectorAll(".stats__btns__item");
Array.from(statsBtnItem).forEach((button) => {
    button.addEventListener('click', () => {
        toggleActive(button);
    });
});