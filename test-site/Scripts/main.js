const myImage = document.querySelector("img");

myImage.addEventListener("click", () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "Images/dodge.jpg") {
    myImage.setAttribute("src", "Images/wallpaper.png");
  } else {
    myImage.setAttribute("src", "Images/dodge.jpg");
  }
});

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
  const myName = prompt("Please enter your name");
  localStorage.setItem("name", myName);
  myHeading.textContent = "FEEL THE POWER OF THE RIDE, ${myName}";
}
if (!localStorage.getItem("name")) {
  setUserNamea();
} else {
  const storedName = localStorage.getItem("name");
  myHeading.textContent = "FEEL THE POWER OF THE RIDE, ${storedName}";
}
myButton.addEventListener("click", () => {
  setUserName();
});
