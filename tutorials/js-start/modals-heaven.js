const openCodeModal = document.getElementById("open-code-modal")
const closeCodeModal = document.getElementById("close-code-modal")
const codeDialog = document.getElementById("code-dialog")


openCodeModal.addEventListener('click', () => {
    codeDialog.showModal();
});

closeCodeModal.addEventListener('click', () => {
    codeDialog.close();
});