// Toggling Skill Tabs

const tabs = document.querySelectorAll('[data-target]');
const tabContent = document.querySelectorAll('[data-content]');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target);

        tabContent.forEach(tabContents => {
            tabContents.classList.remove('skills-active');
        })

        target.classList.add('skills-active');

        tabs.forEach(tab => {
            tab.classList.remove('skills-active');
        })

        tab.classList.add('skills-active');
    })
})

//Mix it up Sorting

let mixerPortfolio = mixitup('.work-container', {
    selectors: {
        target: '.work-card'
    },
    animation: {
        duration: 300
    }
});

// Active link changing

const linkWork = document.querySelectorAll('.work-item');

function activeWork() {
    linkWork.forEach(l => l.classList.remove('active-work'))
    this.classList.add('active-work')
}
linkWork.forEach(l => l.addEventListener('click', activeWork));

//Portfolio Popup

let currentPortfolioItemIndex = 0;
const portfolioItems = document.querySelectorAll('.work-card');

document.addEventListener('click', (e) => {
    if(e.target.classList.contains('work-button')){
        togglePortfolioPopup();
        currentPortfolioItemIndex = Array.from(portfolioItems).indexOf(e.target.parentElement);
        portfolioItemDetails(portfolioItems[currentPortfolioItemIndex]);
    }
});

function togglePortfolioPopup() {
    const popup = document.querySelector('.portfolio-popup');
    popup.classList.toggle('open');
    if(!popup.classList.contains('open')) {
        document.querySelector('.portfolio-popup-video').pause();
        document.querySelector('.portfolio-popup-iframe').src = "";
    }
}

document.querySelector('.portfolio-popup-close').addEventListener('click', togglePortfolioPopup);

document.querySelector('.portfolio-popup').addEventListener('click', (e) => {
    if(e.target.classList.contains('portfolio-popup')){
        togglePortfolioPopup();
    }
});

document.querySelector('.portfolio-popup-video').addEventListener('click', function() {
    if(this.paused) {
        this.play();
    } else {
        this.pause();
    }
});

document.querySelector('.portfolio-popup-next').addEventListener('click', () => {
    let nextIndex = currentPortfolioItemIndex + 1;
    let found = false;
    while(nextIndex < portfolioItems.length) {
        if(window.getComputedStyle(portfolioItems[nextIndex]).display !== 'none') {
            currentPortfolioItemIndex = nextIndex;
            found = true;
            break;
        }
        nextIndex++;
    }
    if(!found) {
        nextIndex = 0;
        while(nextIndex <= currentPortfolioItemIndex) {
            if(window.getComputedStyle(portfolioItems[nextIndex]).display !== 'none') {
                currentPortfolioItemIndex = nextIndex;
                break;
            }
            nextIndex++;
        }
    }
    portfolioItemDetails(portfolioItems[currentPortfolioItemIndex]);
});

function portfolioItemDetails(portfolioItem) {
    const videoType = portfolioItem.dataset.videoType;
    const videoSrc = portfolioItem.dataset.videoSrc || portfolioItem.querySelector('.work-img').src;
    
    const popupVideo = document.querySelector('.portfolio-popup-video');
    const popupIframe = document.querySelector('.portfolio-popup-iframe');

    if (videoType === 'youtube') {
        popupVideo.style.display = 'none';
        popupIframe.style.display = 'block';
        popupIframe.src = videoSrc;
    } else {
        popupIframe.style.display = 'none';
        popupVideo.style.display = 'block';
        popupVideo.src = videoSrc;
    }

    document.querySelector('.portfolio-popup-subtitle span').innerHTML = portfolioItem.querySelector('.work-title').innerHTML;
    document.querySelector('.portfolio-popup-body').innerHTML = portfolioItem.querySelector('.portfolio-item-details').innerHTML;
}

//Services Popup
const modalViews = document.querySelectorAll('.services-modal');
const modelBtns = document.querySelectorAll('.services-button');
const modalCloses = document.querySelectorAll('.services-modal-close');

let modal = function(modalClick) {
    modalViews[modalClick].classList.add('active-modal');
}

modelBtns.forEach((modelBtn, i) => {
    modelBtn.addEventListener('click', () => {
        modal(i);
    })
})

modalCloses.forEach((modalClose) => {
    modalClose.addEventListener('click', () => {
        modalViews.forEach((modalView) => {
            modalView.classList.remove('active-modal');
        })
    })
})

//Swiper Testimonial

let swiper = new Swiper(".testimonials-container", {
    spaceBetween: 24,
    loop: true,
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
        576: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 48,
        },
    },
});

// Input Animation

const inputs = document.querySelectorAll('.input');

function focusFunc() {
    let parent = this.parentNode;
    parent.classList.add('focus');
}

function blurFunc() {
    let parent = this.parentNode;
    if(this.value == "") {
        parent.classList.remove('focus');
    }
}

inputs.forEach((input) => {
    input.addEventListener('focus', focusFunc);
    input.addEventListener('blur', blurFunc);
})

// Scroll Section Active Link

const sections = document.querySelectorAll('section[id]');

window.addEventListener('scroll', navHighlighter);

function navHighlighter() {
    let scrollY = window.scrollY;
    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - (window.innerHeight / 3);
        const sectionId = current.getAttribute('id');
        let navLink = document.querySelector('.nav-menu a[href*=' + sectionId + ']');
        if(navLink) {
            if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navLink.classList.add('active-link');
            } else {
                navLink.classList.remove('active-link');
            }
        }
    });
}

// Activating Sidebar

const navMenu = document.getElementById('sidebar');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');

if(navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-sidebar');
    })
}

if(navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-sidebar');
    })
}