// you can store various data types even other arrays. also objects
const sequence = [1, 1, 2, 3, , 5, 7, 11, 13];
const random = ["tree", 455, 7, [0, 1, 2]];

//
const shopping = ["bread", "milk", "cheese", "hummus", "noodles"];
console.log(shopping);
//finding number of items in shopping array
console.log(shopping.length); //returns 5

//accessing and modifying arrays
console.log(shopping[0]); //returns 'bread'

shopping[0] = "tahini";
console.log(shopping); //used "tahini" at index[0] replacing bread

//add items using push()
const cities = ["Manchester", "Liverpool"];
cities.push("cardiff");
console.log(cities); //added "cardiff"
const newLength = cities.push("bristol");
console.log(newLength); //shows 4 instead of the old number 2

//adding items at the start of the array using unshift()
cities.unshift("Edinburgh");

//removing items using pop()
cities.pop();
console.log(cities);
const removedCity = cities.pop();
console.log(removedCity); //shows cardiff was removed

//using splice() to remove an item if you know its index
const index = cities.indexOf("Liverpool");
if (index !== -1) {
  cities.splice(index, 1); // first argument says where to start removing while the second says how many instances should be removed
}
console.log(cities); //returns without liverpool

//Accessing every item using for...of
const birds = ["parrot", "falcon", "owl"];

for (const bird of birds) {
  console.log(bird);
}

//Using map method to access each item with a function to applied and create a new array
function double(number) {
  return number * 2;
}
const numbers = [5, 2, 7, 6];
const doubled = numbers.map(double);
console.log(doubled); //[10,4,14,12]

//Using filter() to return a new array that meets a certain condition
function isLong(city) {
  return city.length > 8;
}
const longer = cities.filter(isLong);
console.log(longer); //returns only edinburgh and manchester because their length is greater than 8
//
//
//converting between arrays and strings...using split()
const data = "Manchester,London,Liverpool,Birmingham,Leeds,Carlisle";
const citiesSplit = data.split(",");
citiesSplit;
console.log(citiesSplit.length);
console.log(citiesSplit[0]);
console.log(citiesSplit[1]);
console.log(citiesSplit[citiesSplit.length - 1]); //last city split

//converting to string using toString()
const dogNames = ["Rocket", "Flash", "Bella", "Slugger"];
const stringNames = dogNames.toString();
console.log(stringNames);
