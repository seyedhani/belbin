document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".navList li").forEach((item) => {
      const line = item.querySelector(".line");
      const link = item.querySelector("a");
  
      item.addEventListener("mouseover", () => {
        const linkWidth = link.offsetWidth;
        const linkOffsetLeft = link.offsetLeft;
        line.style.width = `${linkWidth}px`;
        line.style.left = `${linkOffsetLeft}px`;
        line.style.opacity = "1";
      });
  
      item.addEventListener("mouseleave", () => {
        line.style.width = "0";
        line.style.opacity = "0";
      });
    });
  });