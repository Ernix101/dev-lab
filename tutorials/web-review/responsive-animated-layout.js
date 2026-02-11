function toggleSubMenu(button){
    button.nextElementSibling.classlist.toggle('show');
}





// const buttonOne = document.querySelector(".dropdown-btn.one")
// const buttonTwo = document.querySelector(".dropdown-btn.two")
// const subMenu = document.querySelector(".submenu")



// function toggleSubMenu(button) {
//     subMenu = button.nextElementSibling;
//     subMenu.classList.toggle("show");
// }

// buttonOne.addEventListener("click", () => {
//     toggleSubMenu(buttonOne)
// })
// buttonTwo.addEventListener("click", () => {
//     toggleSubMenu(buttonTwo)
// })
// document.querySelectorAll(".dropdown-btn").forEach(button => {
//     button.addEventListener("click", (e) => {
//         const submenu = e.currentTarget.parentElement.querySelector(".submenu");
//         if(submenu) subMenu.classlist.toggle("show");
//     });
// });
// document.querySelectorAll('.dropdown-btn').forEach((button, i) => {
//     console.log(`Button ${i} -->`, button.nextElementSibling);
// });

// document.querySelectorAll(".dropdown-btn").forEach((button) => {
//     button.addEventListener("click", e => {
//         const submenu = e.currentTarget.nextElementSibling;
//         submenu.classlist.toggle("show");
//         console.log("Toggled:", submenu.classlist);
//     });
// });