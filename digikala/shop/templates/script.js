document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".navList li").forEach((item) => {
      const line = item.querySelector(".line");
      const link = item.querySelector("a");
  
      function updateLine() {
        // محاسبه موقعیت و اندازه تگ <a>
        const linkRect = link.getBoundingClientRect();
        const itemRect = item.getBoundingClientRect();
  
        // تنظیم موقعیت و اندازه خط
        line.style.width = `${linkRect.width}px`;
        line.style.left = `${linkRect.left - itemRect.left}px`;
        line.style.top = `${linkRect.bottom - itemRect.top - 1}px`; // کاهش فاصله خط از پایین متن
      }
  
      // به‌روزرسانی موقعیت خط
      updateLine();
      window.addEventListener("resize", updateLine);
  
      // به‌روزرسانی موقعیت خط و نمایش آن هنگام هاور
      item.addEventListener("mouseover", () => {
        updateLine(); // به‌روزرسانی موقعیت خط هنگام هاور
        line.style.opacity = "1"; // نمایش خط
      });
  
      // پنهان کردن خط هنگام خارج شدن موس از روی عنصر
      item.addEventListener("mouseleave", () => {
        line.style.opacity = "0"; // محو کردن خط
      });
    });
  });
  