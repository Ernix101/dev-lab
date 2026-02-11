const buttonAdd = document.getElementById("myBtn");
const paraOne = document.getElementById("myParaOne");
const paraTwo = document.getElementById("myParaTwo");
const buttonReset = document.getElementById("myBtnTwo");
const readButton = document.getElementById("readBtn");
let timeoutId;

function ChangeContent() {
  paraOne.textContent = "You have brought the first paragraph to life";
  paraTwo.textContent = "You have brought the second paragraph to life";
}

function removeContent() {
  paraOne.textContent = "";
  paraTwo.textContent = "";
}

let isReading = false;
function MindReader() {
  //
  if (isReading) return Promise.reject(new Error("already reading your mind"));
  isReading = true;
  //
  const thoughtsArray = [
    "You are thinking of You are thinking of NOTHING but FOOD!",
    "Your mind is full of code!",
    "You're dreaming of a VACATION!",
    "Numbers are swirling in your head!",
  ];
  const randomIndex = Math.floor(Math.random() * thoughtsArray.length);

  const randomDelay = Math.floor(Math.random() * 4000) + 2000;

  const randdomColor = `rgb(${Math.floor(Math.random() * 256)}), ${Math.floor(
    Math.random() * 256
  )}, ${Math.floor(Math.random() * 256)}`;

  return new Promise((resolve, reject) => {
    try {
      timeotId = setTimeout(() => {
        const thoughts = document.createElement("p");
        thoughts.textContent = thoughtsArray[randomIndex];
        thoughts.style.backgroundColor = randdomColor;
        document.body.appendChild(thoughts);
        resolve(thoughts.textContent);
        isReading = false;
      }, randomDelay);
    } catch {
      isReading = false;
      reject(new Error("Mind reading failed"));
    }
  });
}

buttonAdd.classList.add("enabled");
buttonReset.classList.add("enabled");

buttonAdd.addEventListener("click", (event) => {
  event.target.classList.replace("enabled", "disabled");
});
buttonReset.addEventListener("click", (event) => {
  if (event.target.classList.contains("disabled")) {
    event.target.textContent += "😡";
  } else {
    event.target.classList.replace("enabled", "disabled");
  }
});

buttonAdd.addEventListener("click", ChangeContent);
buttonAdd.addEventListener("mouseover", (event) => {
  event.target.classList.toggle("hover");
});
buttonAdd.addEventListener("mouseout", (event) => {
  event.target.classList.toggle("hover");
});

buttonReset.addEventListener("mouseover", (event) => {
  event.target.classList.toggle("hover");
});
buttonReset.addEventListener("mouseout", (event) => {
  event.target.classList.toggle("hover");
});

buttonReset.addEventListener("click", () => {
  removeContent();
  if (timeoutId) {
    clearTimeout(timeoutId);
    timeotId = null;
  }
  //remove thoughts if any exist
  const thoughts = document.querySelector("p:last-child");
  if (thoughts && !paraOne.contains(thoughts) && !paraTwo.contains(thoughts)) {
    thoughts.remove();
  }
  isReading = false;
});
readButton.addEventListener("click", () => {
  MindReader()
    .then((message) => {
      console.log(message);
    })
    .catch((error) => console.log(error.message));
  isReading = false;
});
