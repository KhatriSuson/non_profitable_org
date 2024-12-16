// Dark and Light Mode Toggle
const themeToggle = document.getElementById("theme-toggle");
const body = document.body;

// Set the theme from localStorage
if(localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
    themeToggle.textContent = "🌙";
} else {
    body.classList.remove("dark-mode");
    themeToggle.textContent = "🌞";
}

// Toggle theme on button click
themeToggle.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    const theme = body.classList.contains("dark-mode") ? "dark" : "light";
    localStorage.setItem("theme", theme);
    themeToggle.textContent = theme === "dark" ? "🌙" : "🌞";
});

// Language Selector
const languageSelector = document.getElementById("language-selector");

const languageContent = {
    en: {
        heroTitle: "Empowering Youth in Honor of Nepal's Martyrs",
        heroSubtitle: "Building a better future through sports, social work, and community service.",
        ctaButton: "Join Our Mission"
    },
    np: {
        heroTitle: "नेपालका शहीदहरूको सम्मानमा युवा सशक्तिकरण",
        heroSubtitle: "खेलकुद, सामाजिक कार्य, र सामुदायिक सेवामा भविष्य निर्माण।",
        ctaButton: "हाम्रो मिशनमा सामेल हुनुहोस्"
    }
};

// Load selected language
const loadLanguage = (language) => {
    document.getElementById("hero-title").textContent = languageContent[language].heroTitle;
    document.getElementById("hero-subtitle").textContent = languageContent[language].heroSubtitle;
    document.getElementById("cta-button").textContent = languageContent[language].ctaButton;
};

// Set the language from localStorage
if(localStorage.getItem("language") === "np") {
    languageSelector.value = "np";
    loadLanguage("np");
} else {
    languageSelector.value = "en";
    loadLanguage("en");
}

// Change language on selection
languageSelector.addEventListener("change", (event) => {
    const selectedLanguage = event.target.value;
    loadLanguage(selectedLanguage);
    localStorage.setItem("language", selectedLanguage);
});

// Scroll-to-Top Button
const scrollTopButton = document.createElement('button');
scrollTopButton.id = "scroll-top";
scrollTopButton.textContent = "↑";
document.body.appendChild(scrollTopButton);

window.addEventListener("scroll", () => {
    if (window.scrollY > 100) {
        scrollTopButton.style.display = "block";
    } else {
        scrollTopButton.style.display = "none";
    }
});

scrollTopButton.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});
