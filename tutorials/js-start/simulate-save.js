window.onload = function () {
  const button = document.getElementById("myBtn");
  const para = document.getElementById("myPara");

  const createSave = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        para = para.textContent = "YOU HAVE SAVED EVERYTHING!";
      }, 3000);
    });
  };

  button.addEventListener("click", () => {
    createSave();
  });
};
