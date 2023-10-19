const container = document.querySelector('.container');
const signupLink = document.querySelector('#signuplink');
const signinLink = document.querySelector('#signinlink');

signupLink.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent the default link behavior
    container.classList.add('active');

    // Listen for the transition end event
    container.addEventListener('transitionend', () => {
        window.location.href = '/register'; // Navigate to the registration page
    }, { once: true });
});

signinLink.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent the default link behavior
    container.classList.remove('active');

    // Listen for the transition end event
    container.addEventListener('transitionend', () => {
        window.location.href = '/login'; // Navigate to the login page
    }, { once: true });
});
