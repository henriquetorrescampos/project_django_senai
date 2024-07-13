const btn = document.querySelector("#theme-toggle");
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
const prefersLightScheme = window.matchMedia("(prefers-color-scheme: light)");

let currentTheme = localStorage.getItem("theme");

function setTheme() {
    if (currentTheme === null) {
        if (prefersDarkScheme.matches) {
            currentTheme = "dark";
        } else if (prefersLightScheme.matches) {
            currentTheme = "light";
        } else {
            currentTheme = "dark"; // Default to dark if no preference found
        }
    }

    if (currentTheme === "dark") {
        document.body.classList.remove("light-mode");
        document.body.classList.add("dark-mode");
    } else if (currentTheme === "light") {
        document.body.classList.remove("dark-mode");
        document.body.classList.add("light-mode");
    }
}

btn.addEventListener("click", function () {
    if (currentTheme === "dark") {
        currentTheme = "light";
    } else {
        currentTheme = "dark";
    }
    setTheme();
    localStorage.setItem("theme", currentTheme);
});

setTheme();