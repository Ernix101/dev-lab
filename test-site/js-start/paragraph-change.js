window.onload = function () {
  const p1 = document.getElementById("myParaOne");
  const p2 = document.getElementById("myParaTwo");
  const reset = document.getElementById("reset");
  const button = document.getElementById("mybtn");

  console.log("p1:", p1, "p2:", "button:", button);

  const changeLook1 = () => {
    p1.style.backgroundColor = "green";
    p1.textContent = "You just brought p1 to life.";
  };

  const changeLook2 = () => {
    p2.style.backgroundColor = "green";
    p2.textContent = "You just brought p2 to life.";
  };

  const delayedChange = () => {
    return new Promise((resolve, reject) => {
      if (!p1 || !p2 || !button) {
        reject(new Error("Elements Not Found!"));
        return;
      }

      //simulate a condition (eg. random boolean for demo using a math algorithm)
      const success = Math.random() > 0.5;

      setTimeout(() => {
        if (success) {
          changeLook1();
          changeLook2();
          resolve();
        } else {
          reject(new Error("failed to update paragraphs"));
        }
      }, 3000); // 3 second delay
    });
  };

  button.addEventListener("click", () => {
    p1.textContent = "Loading...";
    p2.textContent = "Loading...";

    delayedChange()
      .then(() => {
        //No action needed on success, changes are already applied
      })
      .catch((error) => {
        p1.textContent = "Error " + error.message;
        p2.textContent = "Error " + error.message;
      });
  });
};
