
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menuToggle");
  const mobileNav = document.getElementById("mobileNav");
  if (menuToggle && mobileNav) {
    menuToggle.addEventListener("click", () => mobileNav.classList.toggle("open"));
  }

  const lightbox = document.getElementById("lightbox");
  const lightboxImage = document.getElementById("lightboxImage");
  const lightboxTitle = document.getElementById("lightboxTitle");
  const closeBtn = document.getElementById("lightboxClose");
  const prevBtn = document.getElementById("lightboxPrev");
  const nextBtn = document.getElementById("lightboxNext");
  const items = Array.from(document.querySelectorAll(".gallery-item"));
  let currentIndex = 0;

  function openLightbox(index) {
    if (!items.length) return;
    currentIndex = index;
    const item = items[currentIndex];
    const img = item.querySelector("img");
    lightboxImage.src = img.src;
    lightboxImage.alt = img.alt || "";
    lightboxTitle.textContent = item.dataset.title || img.alt || "";
    lightbox.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  }

  function move(step) {
    if (!items.length) return;
    currentIndex = (currentIndex + step + items.length) % items.length;
    openLightbox(currentIndex);
  }

  items.forEach((item, index) => item.addEventListener("click", () => openLightbox(index)));
  if (closeBtn) closeBtn.addEventListener("click", closeLightbox);
  if (prevBtn) prevBtn.addEventListener("click", () => move(-1));
  if (nextBtn) nextBtn.addEventListener("click", () => move(1));
  if (lightbox) lightbox.addEventListener("click", (e) => { if (e.target === lightbox) closeLightbox(); });

  document.addEventListener("keydown", (e) => {
    if (!lightbox || !lightbox.classList.contains("open")) return;
    if (e.key === "Escape") closeLightbox();
    if (e.key === "ArrowLeft") move(-1);
    if (e.key === "ArrowRight") move(1);
  });
});
/* =========================
   TEAM SPOTLIGHT SLIDER
========================= */
document.addEventListener("DOMContentLoaded", () => {
  const spotlightImage = document.getElementById("teamSpotlightImage");
  const spotlightName = document.getElementById("teamSpotlightName");
  const spotlightCount = document.getElementById("teamSpotlightCount");
  const prevBtn = document.getElementById("teamPrevBtn");
  const nextBtn = document.getElementById("teamNextBtn");
  const thumbButtons = Array.from(document.querySelectorAll(".team-thumb-btn"));

  const teamsModal = document.getElementById("teamsModal");
  const openTeamsModal = document.getElementById("openTeamsModal");
  const closeTeamsModal = document.getElementById("closeTeamsModal");
  const teamsModalOverlay = document.getElementById("teamsModalOverlay");

  if (!spotlightImage || !spotlightName || !spotlightCount || !thumbButtons.length) {
    return;
  }

  const teams = thumbButtons.map((btn) => ({
    name: btn.dataset.name,
    file: btn.dataset.file,
  }));

  let currentIndex = 0;

  function formatCount(index, total) {
    const current = String(index + 1).padStart(2, "0");
    const max = String(total).padStart(2, "0");
    return `${current} / ${max}`;
  }

  function setActiveThumb(index) {
    thumbButtons.forEach((btn, i) => {
      btn.classList.toggle("active", i === index);
    });
  }

  function renderTeam(index) {
    const team = teams[index];
    if (!team) return;

    currentIndex = index;
    spotlightImage.src = team.file;
    spotlightImage.alt = team.name;
    spotlightName.textContent = team.name;
    spotlightCount.textContent = formatCount(index, teams.length);
    setActiveThumb(index);
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      const nextIndex = (currentIndex - 1 + teams.length) % teams.length;
      renderTeam(nextIndex);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      const nextIndex = (currentIndex + 1) % teams.length;
      renderTeam(nextIndex);
    });
  }

  thumbButtons.forEach((btn, index) => {
    btn.addEventListener("click", () => renderTeam(index));
  });

  if (openTeamsModal && teamsModal) {
    openTeamsModal.addEventListener("click", () => {
      teamsModal.classList.add("open");
      document.body.style.overflow = "hidden";
    });
  }

  function closeModal() {
    if (!teamsModal) return;
    teamsModal.classList.remove("open");
    document.body.style.overflow = "";
  }

  if (closeTeamsModal) {
    closeTeamsModal.addEventListener("click", closeModal);
  }

  if (teamsModalOverlay) {
    teamsModalOverlay.addEventListener("click", closeModal);
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && teamsModal && teamsModal.classList.contains("open")) {
      closeModal();
    }

    if (e.key === "ArrowLeft") {
      const nextIndex = (currentIndex - 1 + teams.length) % teams.length;
      renderTeam(nextIndex);
    }

    if (e.key === "ArrowRight") {
      const nextIndex = (currentIndex + 1) % teams.length;
      renderTeam(nextIndex);
    }
  });

  renderTeam(0);
});
