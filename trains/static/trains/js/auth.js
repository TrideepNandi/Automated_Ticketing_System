const container = document.querySelector('.container');
const LoginLink = document.querySelector('.signinlink');
const RegisterLink = document.querySelector('.signuplink');

RegisterLink.addEventListener('click', () => {
    container.classList.add('active');

    // Wait for the transition to complete before changing the URL
    setTimeout(() => {
        history.pushState({}, '', '/register/');
    }, 71); // Adjust the timeout duration as needed (in milliseconds)
});

LoginLink.addEventListener('click', () => {
    container.classList.remove('active');

    // Wait for the transition to complete before changing the URL
    setTimeout(() => {
        history.pushState({}, '', '/login/');
    }, 71); // Adjust the timeout duration as needed (in milliseconds)
});