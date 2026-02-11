const customName = document.getElementById("customname");
const randomize = document.querySelector(".randomize");
const story = document.querySelector(".story");
const ukRadio = document.getElementById("uk");
let newStory;
let weight;
let temperature;

//const replacedName = randomValueFromArray(insertx);

const storyText =
  "It was 94 farenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing but was not surprised - :insertx: weighs 300 pounds and it was a hot day.";

const insertx = ["Willy the Goblin", "Big Daddy", "Father Christmas"];

const inserty = ["the soup kitchen", "Disney", "the White house"];

const insertz = [
  "spontaneously combusted",
  "melted into a puddle on the sidewalk",
  "turned into a slug and crawled away",
];

function randomValueFromArray(array) {
  const random = Math.floor(Math.random() * array.length);
  return array[random];
}

// Event Listener and partial function definition
randomize.addEventListener("click", result);

function result() {
  let newStory = storyText;

  let xitem = randomValueFromArray(insertx);
  let yitem = randomValueFromArray(inserty);
  let zitem = randomValueFromArray(insertz);

  newStory = newStory.replace(/:insertx:/g, xitem);
  newStory = newStory.replace(":inserty:", yitem);
  newStory = newStory.replace(":insertz:", zitem);

  // if (ukRadio && ukRadio.checked) {
  //   const weight = Math.round(300 * 0.0714286) + ` stone`;
  //   const temperature = Math.round((94 - 32) * (5 / 9)) + ` centigrade`;
  // }

  if (customName.value !== "") {
    const name = customName.value;
    newStory = newStory.replace("Bob", name);
  }

  //  newStory = newStory.replace(`300 pounds`, weight);
  //  newStory = newStory.replace(`94 farenheit`, temperature);

  story.textContent = newStory;
  story.style.visibility = "visible";
}

const clicked = document.querySelector(".clicked");
const parentDiv = document.querySelector(".parent-div");

clicked.addEventListener("click", (event) => {
  console.log("BUTTON clicked");
  event.stopPropagation();
});
parentDiv.addEventListener("click", (event) => {
  console.log("DIV clicked");
});
