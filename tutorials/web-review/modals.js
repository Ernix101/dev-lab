const openBtn = document.getElementById("open-modal");
const dialog = document.getElementById("dialog");
const closeBtn = document.getElementById("close-modal");


openBtn.addEventListener('click', () => {
    dialog.showModal();
})

closeBtn.addEventListener('click', () => {
    dialog.close();
});

// Close the modal when clicking outside or on the backdrop
dialog.addEventListener('click', event => {
    const rect = dialog.getBoundingClientRect();
    const isInDialog =
        event.clientX >= rect.left &&
        event.clientX >= rect.right &&
        event.clientY >= rect.top &&
        event.clientY >= rect.bottom;

    if (!isInDialog) {
        dialog.close();
    }
});