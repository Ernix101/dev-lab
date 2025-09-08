const browserType = "mozilla";
typeLength = browserType.length;

console.log(typeLength);
//Testing if a string contains a substring...includes,startwith,endswith
if (browserType.endsWith("zilla")) {
  console.log("found zilla");
} else {
  console.log("No zilla here");
}

//Finding position of a substring
const tagline = "MDN - Resources for developers, By developers";
console.log(tagline.indexOf("developers"));

const firstOccurrence = tagline.indexOf("developers");
const secondOcccurrence = tagline.indexOf("developers", firstOccurrence + 1);

console.log(firstOccurrence);
console.log(secondOcccurrence);

//Extracting a substring from a string...slice from 'mozilla'

console.log(browserType.slice(1, 4));
console.log(browserType.slice(2));

//Changing case...toLowerCase or toUpperCase
const radData = "My name is MuD";
console.log(radData.toLocaleUpperCase());
console.log(radData.toLowerCase());

//Updating parts of a string...replace or replaceAll
const updated = browserType.replace("moz", "van");
console.log(updated);
console.log(browserType);

// Learning challenges!!!
// filtering greeting messages
const list = document.querySelector("ul");
const greetings = [
  "Happy Birthday!",
  "Merry Christmas my love",
  "You're all I want for christmas",
  "Get well soon",
];

for (const greeting of greetings) {
  if (greeting.includes("Christmas")) {
    const listItem = document.createElement("li");
    listItem.textContent = greeting;
    list.appendChild(listItem);
  }
}
//Fixing Capitalization
const list1 = document.querySelector("ul");
const cities = ["lonDon", "ManChESTer", "BiRmiNGHAM", "liVERpoOL"];

for (const city of cities) {
  const lower = city.toLowerCase();
  const firstLetter = lower.slice(0, 1);
  const capitalized = lower.replace(firstLetter, firstLetter.toUppercase());
  const result = capitalized;
  const listItem = document.createElement("li");
  listItem.textContent = result;
  list.appendChild(listItem);
}

//Making new strings from old parts
const list2 = document.querySelector("ul");
const stations = [
  "MAN675847583748sjt5775;Manchester Picadilly",
  "GNF57488874774778yhy88;Liverpool Lime Street",
  "LIV57474674746vvfhf748;Stalybridge",
  "HUD576747y4760jjfjfn56;Huddersfield",
];

for (const station of stations) {
  firstLetters = station.slice(0, 3);
  index = station.indexOf(";");
  substring = station.slice(index + 1);
  combined = `${firstLetters}; ${substring}`;
  const listItem = document.createElement("li");
  listItem.textContent = combined;
  list.appendChild(listItem);
}
