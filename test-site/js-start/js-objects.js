let user = {
  name: "Ernest",
  age: 20,
  city: "Nairobi",
  greet: function () {
    console.log("hello my name is" + this.name);
  },
};
user.greet(); // "Hello, my name is Ernest"

let cart = [
  { item: "shoes", price: 3000 },
  { item: "shirt", price: 1500 },
];
console.log(cart[1].item); //shoes.

// Update a property using dot notation
user.age = 21;

// Update a property using bracket notation
user["city"] = "Machakos";

console.log(user);
//adding a property
user.email = "ernest@gmail.com";
console.log(user);
//
//Example of array objects
let users = [
  { FirstName: "Ernest", age: 21 },
  { FirstName: "Shannon", age: 22 },
];
//
// To add (push) a new user
users.push({ FirstName: "carl", age: 25 });
console.log(users);
//
// Using bracket notation with variables
let propertyToUpdate = "FirstName";
users[0][propertyToUpdate] = "Erns";
console.log(users[0]);
//
// A Mini User Database
let data = [];
let username = window.prompt("Enter your name");
username =
  username.trim().charAt(0).toUpperCase() + username.slice(1).toLowerCase();
let userObj = {
  name: username,
};
//
//data.push(userObj);
//
let email = window.prompt("Enter your email");
userObj = {
  name: username,
  email: email,
};
//data.push(userObj);
let age = window.prompt("enter age");
userObj = {
  name: username,
  email: email,
  age: age,
};
data.push(userObj);

console.log(data);
