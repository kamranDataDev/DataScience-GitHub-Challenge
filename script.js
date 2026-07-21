const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const siteHeader = document.querySelector(".site-header");
const yearElement = document.querySelector("#year");
const revealElements = document.querySelectorAll(".reveal");
const sectionLinks = document.querySelectorAll('.nav-links a[href^="#"]');
const heroHeading = document.querySelector(".hero-content h1");

yearElement.textContent = new Date().getFullYear();

if (heroHeading) {
  const typingContainer = document.createElement("p");
  const typingText = document.createElement("span");
  const typingCursor = document.createElement("span");

  typingContainer.setAttribute("aria-live", "polite");
  typingContainer.style.margin = "-0.2rem 0 1.15rem";
  typingContainer.style.fontWeight = "700";
  typingContainer.style.fontSize = "clamp(1rem, 1.9vw, 1.25rem)";
  typingContainer.style.letterSpacing = "0.01em";
  typingContainer.style.color = "rgba(245, 252, 255, 0.92)";

  typingCursor.textContent = "|";
  typingCursor.setAttribute("aria-hidden", "true");
  typingCursor.style.display = "inline-block";
  typingCursor.style.marginLeft = "0.25rem";
  typingCursor.style.opacity = "1";
  typingCursor.style.transition = "opacity 120ms linear";

  typingContainer.append(typingText, typingCursor);
  heroHeading.insertAdjacentElement("afterend", typingContainer);

  const roles = [
    "Flutter Developer",
    "Data Scientist",
    "Machine Learning Enthusiast",
    "AI Learner",
  ];

  let roleIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  const tick = () => {
    const currentRole = roles[roleIndex];

    if (isDeleting) {
      charIndex -= 1;
    } else {
      charIndex += 1;
    }

    typingText.textContent = currentRole.slice(0, charIndex);

    let delay = isDeleting ? 55 : 95;

    if (!isDeleting && charIndex === currentRole.length) {
      delay = 1300;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      delay = 320;
    }

    window.setTimeout(tick, delay);
  };

  window.setInterval(() => {
    typingCursor.style.opacity = typingCursor.style.opacity === "0" ? "1" : "0";
  }, 520);

  tick();
}

const syncHeaderState = () => {
  siteHeader.classList.toggle("is-scrolled", window.scrollY > 12);
};

syncHeaderState();
window.addEventListener("scroll", syncHeaderState, { passive: true });

menuToggle.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("is-open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

sectionLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    const target = document.querySelector(link.getAttribute("href"));
    if (target) {
      event.preventDefault();
      const offset = siteHeader.offsetHeight + 8;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: "smooth" });
    }

    if (window.matchMedia("(max-width: 760px)").matches) {
      navLinks.classList.remove("is-open");
      menuToggle.setAttribute("aria-expanded", "false");
    }
  });
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.15,
  },
);

revealElements.forEach((element) => observer.observe(element));

const highlightedLinks = Array.from(sectionLinks);
const sections = highlightedLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

const activeObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      }

      highlightedLinks.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === `#${entry.target.id}`);
      });
    });
  },
  {
    threshold: 0.45,
    rootMargin: "-15% 0px -55% 0px",
  },
);

sections.forEach((section) => activeObserver.observe(section));