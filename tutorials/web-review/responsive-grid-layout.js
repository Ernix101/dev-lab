const sidebar = document.getElementById("sidebar")
const toggleButton = document.getElementById("toggleSidebar")

toggleButton.addEventListener("click",(e) => {
    toggleSidebar()
})


function toggleSidebar(){
    sidebar.classList.toggle('show')
}