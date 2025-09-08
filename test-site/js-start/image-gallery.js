const featuredImg = document.getElementById("featured");
const toggleBtn = document.querySelector("theme-toggle");
// const panel = document.querySelector("panel");
const randomizeBtn = document.getElementById("randomize");
//Images path
const ImageOne = document.getElementById("img1");
const ImageTwo = document.getElementById("img2");
const ImageThree = document.getElementById("img3");
const ImageFour = document.getElementById("img4");
const ImageFive = document.getElementById("img5");
const ImageSix = document.getElementById("img6");

//
//

const Thumbnails = [
  "/Images/GTA.png",
  "/Images/asphalt9.jpg",
  "/Images/minecraft.jpg",
  "/Images/roblox.jpg",
  "/Images/freefire.jpg",
  "/Images/fortnite.jpg",
];

// Function to change featured image and replace

function changeImg(selector) {
  const randomIndex = Math.floor(Math.random() * Thumbnails.length);
  //Find the image element
  featuredImg.src = Thumbnails[randomIndex];
  //Check if element exists
  if (Thumbnails.length === 0) {
    console.log(`Image element with selector "${selector}" not found`);
    return;
  }
  // some extras not major in the challenge
  featuredImg.classList.add("hidden");
  setTimeout(() => {
    featuredImg.src = Thumbnails[randomIndex];
    featuredImg.classList.remove("hidden");
  }, 500);
}
//
//
// toggleBtn.addEventListener("click", () => {
//   document.body.classList.backgroundColor = "black";
// });
randomizeBtn.addEventListener("click", changeImg);
//
ImageOne.addEventListener("click", () => {
  featuredImg.src = Thumbnails[0];
});
ImageTwo.addEventListener("click", () => {
  featuredImg.src = Thumbnails[1];
});
ImageThree.addEventListener("click", () => {
  featuredImg.src = Thumbnails[2];
});
ImageFour.addEventListener("click", () => {
  featuredImg.src = Thumbnails[3];
});
ImageFive.addEventListener("click", () => {
  featuredImg.src = Thumbnails[4];
});
ImageSix.addEventListener("click", () => {
  featuredImg.src = Thumbnails[5];
});
//
// Some Extras...
