document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".login").onmouseover = () => {
        document.querySelector(".user").blur();
        document.querySelector(".password").blur();
    }

    document.querySelector(".newaccount").onmouseover = () => {
        document.querySelector(".user").blur();
        document.querySelector(".password").blur();
    }
});
