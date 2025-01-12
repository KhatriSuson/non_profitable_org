// Dark/Light Mode Toggle
 // Get the theme toggle button and body element
 const themeToggleButton = document.getElementById("theme-toggle");
 const body = document.body;

 // Check the user's saved theme preference from localStorage
 const savedTheme = localStorage.getItem("theme");

 // Apply the saved theme on page load
 if (savedTheme) {
     body.classList.add(savedTheme);
 }

 // Event listener for the theme toggle button
 themeToggleButton.addEventListener("click", () => {
     // Toggle between dark and light modes
     body.classList.toggle("dark-mode");

     // Save the user's preference to localStorage
     if (body.classList.contains("dark-mode")) {
         localStorage.setItem("theme", "dark-mode");
         themeToggleButton.innerHTML = "🌞"; // Change button icon for light mode
     } else {
         localStorage.setItem("theme", "light-mode");
         themeToggleButton.innerHTML = "🌙"; // Change button icon for dark mode
     }
 });

// Language Toggle
const languageSelector = document.getElementById('language-selector');

const currentLang = localStorage.getItem('lang') || 'en';
languageSelector.value = currentLang;

const translations = {
    en: {
        heroTitle: 'Welcome to Martyrs\' Legacy',
        heroDescription: 'Honoring our martyrs and empowering the youth of Nepal',
        ctaButton: 'Join Us',
        aboutUsTitle: 'About Us',
        aboutDescription: 'We work towards creating a better future for Nepal’s youth...',
        programsTitle: 'Our Programs',
        program1Title: 'Sports',
        program1Description: 'Engaging the youth in sports to build discipline and teamwork.',
        program2Title: 'Social Work',
        program2Description: 'Helping the community through social initiatives and volunteer work.',
        program3Title: 'Addiction Recovery',
        program3Description: 'Working with individuals to overcome addiction and build a brighter future.',
        contactTitle: 'Contact Us',
        sendMessageButton: 'Send Message',
        footerText: '© 2024 Martyrs\' Legacy. All rights reserved.'
    },
    np: {
        heroTitle: 'शहीदहरूको धरोहरमा स्वागत छ',
        heroDescription: 'हाम्रो शहीदहरूको सम्मान र नेपालका युवाहरूसँग सशक्त बनाउनको लागि',
        ctaButton: 'हामीलाई सामेल गर्नुहोस्',
        aboutUsTitle: 'हाम्रो बारेमा',
        aboutDescription: 'हामी नेपालका युवाका लागि राम्रो भविष्य बनाउनको लागि काम गर्दैछौं...',
        programsTitle: 'हाम्रो कार्यक्रमहरू',
        program1Title: 'खेलकुद',
        program1Description: 'युवाहरूलाई अनुशासन र टीमवर्क सिकाउन खेलकुदमा संलग्न गर्नु।',
        program2Title: 'सामाजिक कार्य',
        program2Description: 'सामाजिक पहल र स्वयंसेवा कार्यमार्फत समुदायलाई मद्दत गर्नु।',
        program3Title: 'लत उपचार',
        program3Description: 'लतलाई पार गर्न र उज्जवल भविष्य बनाउन व्यक्तिहरूसँग काम गर्नु।',
        contactTitle: 'संपर्क गर्नुहोस्',
        sendMessageButton: 'सन्देश पठाउनुहोस्',
        footerText: '© 2024 शहीदहरूको धरोहर। सबै अधिकार सुरक्षित।'
    }
};

function changeLanguage(lang) {
    localStorage.setItem('lang', lang);
    document.getElementById('hero-title').textContent = translations[lang].heroTitle;
    document.getElementById('hero-description').textContent = translations[lang].heroDescription;
    document.getElementById('cta-button').textContent = translations[lang].ctaButton;

    document.getElementById('about-us-title').textContent = translations[lang].aboutUsTitle;
    document.getElementById('about-description').textContent = translations[lang].aboutDescription;

    document.getElementById('programs-title').textContent = translations[lang].programsTitle;
    document.getElementById('program-1-title').textContent = translations[lang].program1Title;
    document.getElementById('program-1-description').textContent = translations[lang].program1Description;
    document.getElementById('program-2-title').textContent = translations[lang].program2Title;
    document.getElementById('program-2-description').textContent = translations[lang].program2Description;
    document.getElementById('program-3-title').textContent = translations[lang].program3Title;
    document.getElementById('program-3-description').textContent = translations[lang].program3Description;

    document.getElementById('contact-title').textContent = translations[lang].contactTitle;
    document.getElementById('send-message-button').textContent = translations[lang].sendMessageButton;

    document.getElementById('footer-text').textContent = translations[lang].footerText;
}

languageSelector.addEventListener('change', () => {
    const newLang = languageSelector.value;
    changeLanguage(newLang);
});

// Set the language based on saved preference on page load
changeLanguage(currentLang);

// about js

    // Scroll-triggered animation
    window.addEventListener("scroll", function() {
        const aboutSection = document.getElementById("about-us");
        const aboutContent = document.querySelector(".about-content");

        // Check if the About Us section is in the viewport
        const sectionTop = aboutSection.getBoundingClientRect().top;
        const sectionHeight = aboutSection.offsetHeight;
        const windowHeight = window.innerHeight;

        if (sectionTop < windowHeight - 100) {
            aboutContent.style.opacity = "1";
            aboutContent.style.transform = "translateY(0)";
        }
    });


// get involved js

    // Scroll-triggered animation
    window.addEventListener("scroll", function() {
        const getInvolvedSection = document.getElementById("get-involved");
        const getInvolvedContent = document.querySelector(".get-involved-content");

        // Check if the Get Involved section is in the viewport
        const sectionTop = getInvolvedSection.getBoundingClientRect().top;
        const sectionHeight = getInvolvedSection.offsetHeight;
        const windowHeight = window.innerHeight;

        if (sectionTop < windowHeight - 100) {
            getInvolvedContent.style.opacity = "1";
            getInvolvedContent.style.transform = "translateY(0)";
        }
    });
    // Handle Volunteer Button click to show the signup form with animation
document.getElementById('volunteer-btn').addEventListener('click', function () {
    const signupForm = document.getElementById('signup-form');
    signupForm.classList.add('show');
    signupForm.scrollIntoView({ behavior: 'smooth' });
  });
  
  // Handle Donate Button click to show the donation form
  document.getElementById('donate-btn').addEventListener('click', function () {
    const donateSection = document.getElementById('donate-section');
    donateSection.scrollIntoView({ behavior: 'smooth' });
  });
  

  document.addEventListener("DOMContentLoaded", function() {
    const filterButtons = document.querySelectorAll(".filter-btn");
    const galleryItems = document.querySelectorAll(".gallery-item");

    // Show all images by default
    galleryItems.forEach(item => item.classList.add("show"));

    filterButtons.forEach(button => {
        button.addEventListener("click", function() {
            // Remove 'active' class from all buttons
            filterButtons.forEach(btn => btn.classList.remove("active"));
            this.classList.add("active");

            const category = this.getAttribute("data-category");

            galleryItems.forEach(item => {
                if (category === "all" || item.classList.contains(category)) {
                    item.classList.add("show");
                } else {
                    item.classList.remove("show");
                }
            });
        });
    });
});
