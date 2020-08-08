document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".submit").onmouseover = () => {
        document.querySelector(".user").blur();
        document.querySelector(".password").blur();
    }
});
