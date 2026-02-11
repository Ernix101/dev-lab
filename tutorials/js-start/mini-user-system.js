const userEntry = document.getElementById("username");
const passEntry = document.getElementById("password");
const form = document.querySelector(".loginform");
const messageDiv = document.getElementById("messageDiv");
const signUpBtn = document.getElementById("signUp");
const loginBtn = document.getElementById("loginBtn");

let users = [];
// helper: to normalize username
function formatUsername(name) {
  let trimmed = name.trim();
  return trimmed.charAt(0).toUpperCase() + trimmed.slice(1).toLowerCase();
}

// SIGN UP FUNCTION
function signUp() {
  let username = formatUsername(userEntry.value);
  let password = passEntry.value.trim();

  // Get existing users or initialize empty array
  let users = JSON.parse(localStorage.getItem("users")) || [];

  // check if username already exists

  if (users.some((user) => user.username === username)) {
    messageDiv.textContent = "⚠️ Username already exists!";
    messageDiv.style.color = "red";
    return;
  }

  // add user to the "database"
  users.push({ Username: username, Password: password });

  console.log(users);

  // save back to localstorage
  localStorage.setItem("users", JSON.stringify(users));

  messageDiv.textContent = "✅ Account created for " + username;
  messageDiv.style.color = "green";

  // clear inputs
  userEntry.value = "";
  passEntry.value = "";
}

// LOGIN FUNCTION
function login() {
  let username = formatUsername(userEntry.value);
  let password = passEntry.value.trim();

  let users = JSON.parse(localStorage.getItem("users")) || [];

  // find matching user
  const found = users.find(
    (user) => user.username === username && user.password === password
  );

  if (found) {
    localStorage.setItem("loggedInUser", username); // remember who is logged in

    messageDiv.textContent = "🎉 Welcome back," + username + "!";
    messageDiv.style.color = "red";
  } else {
    messageDiv.textContent = "❌ Invalid username or password!";
    messageDiv.color = "red";
  }
}

// EVENT LISTENERS
signUpBtn.addEventListener("click", signUp);
loginBtn.addEventListener("click", login);
