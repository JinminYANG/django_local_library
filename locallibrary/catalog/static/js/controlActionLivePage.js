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





// streaming controls
const videoPlayer = document.querySelector(".streaming__item")
const video = videoPlayer.querySelector(".streaming__item__video")
const playButton = videoPlayer.querySelector('.play_button')
const volume = videoPlayer.querySelector('.volume__control')
const currentTimeElement = videoPlayer.querySelector('.current')
const durationTimeElement = videoPlayer.querySelector('.duration')
const progress = videoPlayer.querySelector('.video-progress')
const progressBar = videoPlayer.querySelector('.video-progress-filled')

// new
// preferences
const settingButton = videoPlayer.querySelector(".setting_button")
const preferences = videoPlayer.querySelector(".preferences");
settingButton.addEventListener("click", (e) => {
    if (preferences.classList.contains("active")) {
        preferences.classList.remove("active");
    } else {
        preferences.classList.add("active");
    }
})

// full screen
const fullScreenButton = videoPlayer.querySelector(".full_screen_button");

fullScreenButton.addEventListener("click", (e) => {
    toggleFullScreen()
})

function isFullScreen() {
    return (document.fullScreenElement && document.fullScreenElement !== null) ||
        (document.msFullscreenElement && document.msFullscreenElement !== null) ||
        (document.mozFullScreen || document.webkitIsFullScreen);
}

function enterFullScreen() {
    const page = videoPlayer
    if (page.requestFullscreen) {
        page.requestFullscreen();
        // page.classList.add("active");
        toggleActive(page);
    } else if (page.mozRequestFullScreen) page.mozRequestFullScreen();
    else if (page.msRequestFullscreen) page.msRequestFullscreen();
    else if (page.webkitRequestFullScreen) page.webkitRequestFullScreen();
}

function exitFullScreen() {
    if (document.exitFullScreen) {
        toggleActive(videoPlayer);
        return document.exitFullScreen();
    } else if (document.webkitExitFullscreen) {
        toggleActive(videoPlayer);
        return document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
        toggleActive(videoPlayer);
        return document.msExitFullscreen();
    } else if (document.mozCancelFullScreen) {
        toggleActive(videoPlayer);
        return document.mozCancelFullScreen();
    }
}

function toggleFullScreen() {
    if (!isFullScreen()) {
        enterFullScreen();
    } else {
        exitFullScreen();
    }
}


const videoPlayerCloseButton = videoPlayer.querySelector(".streaming__item__close")

videoPlayerCloseButton.addEventListener("click", (e) => {
    if (document.exitFullscreen) {
        document.exitFullscreen();
        videoPlayer.classList.remove("active");
    }
})


// Play and Pause button
playButton.addEventListener('click', (e) => {
    if (video.paused) {
        video.play();
        e.target.classList.replace("bi-play-fill", "bi-pause-fill")
    } else {
        video.pause();
        e.target.classList.replace("bi-pause-fill", "bi-play-fill")
    }
})

video.addEventListener("click", (e) => {
    if (video.paused) {
        video.play();
        playButton.children[0].classList.replace("bi-play-fill", "bi-pause-fill");
    } else {
        video.pause();
        playButton.children[0].classList.replace("bi-pause-fill", "bi-play-fill")
    }
})


//volume
volume.addEventListener('mousemove', (e) => {
    video.volume = e.target.value
})

const volumeControl = document.querySelector(".volume__control");

function setBackgroundSize(volumeControl) {
    volumeControl.style.setProperty("--background-size", `${getBackgroundSize(volumeControl)}%`);
}

setBackgroundSize(volumeControl);

volumeControl.addEventListener("input", () => setBackgroundSize(volumeControl));

function getBackgroundSize(volumeControl) {
    const min = +volumeControl.min || 0;
    const max = +volumeControl.max || 100;
    const value = +volumeControl.value;
    const size = (value - min) / (max - min) * 100;

    return size;
}

// share link copy icon

const copyText = document.querySelector(".share_modal__link__text")
const copyIcon = document.querySelector(".share_modal__link__btn__icon")

copyIcon.addEventListener('click', (e) => {
    copyText.select();
    copyText.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(copyText.value);

    copyIcon.classList.replace("bi-stickies", "bi-stickies-fill")

    setTimeout(function() {
        copyIcon.classList.replace("bi-stickies-fill", "bi-stickies")
    }, 5000);
});


// volume control
const volumeButton = document.querySelector(".volume_button")
const leftSideControls = document.querySelector(".player-controls-left")
const volumePanel = document.querySelector('.volume__control__container');

volumeButton.addEventListener("mouseenter", () => {
    volumeControl.classList.add("active")
})

leftSideControls.addEventListener('mouseleave', () => {
    volumeControl.classList.remove("active")
})

volumeButton.addEventListener("click", () => {
    if (video.muted) {
        video.muted = false;
        volumeButton.children[0].classList.replace("bi-volume-down", "bi-volume-mute")
        volumeControl.style.setProperty("--background-size", `0%`);
        volumeControl.setAttribute("value", "0")
    } else {
        video.muted = true;
        volumeButton.children[0].classList.replace("bi-volume-mute", "bi-volume-down")
        volumeControl.style.setProperty("--background-size", `100%`);
        volumeControl.setAttribute("value", "1")
    }
})