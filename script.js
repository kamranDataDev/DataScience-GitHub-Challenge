const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const yearElement = document.querySelector("#year");
const revealElements = document.querySelectorAll(".reveal");
const sectionLinks = document.querySelectorAll('.nav-links a[href^="#"]');

yearElement.textContent = new Date().getFullYear();

menuToggle.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("is-open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

sectionLinks.forEach((link) => {
  link.addEventListener("click", () => {
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