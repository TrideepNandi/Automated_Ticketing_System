const container = document.querySelector('.container');
const LoginLink = document.querySelector('.signinlink');
const RegisterLink = document.querySelector('.signuplink');

RegisterLink.addEventListener('click', () => {
    container.classList.add('active')
});

LoginLink.addEventListener('click', () => {
    container.classList.remove('active')
});