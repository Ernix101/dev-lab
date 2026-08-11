const cards = document.querySelectorAll('.appointment-card');
const drawer = document.querySelector('.patient-drawer');
const drawerClose = document.querySelector('.drawer-close');

cards.forEach(card => {
    card.addEventListener('click', () => {
        drawer.querySelector('.patient-name').textContent = card.dataset.patientName;
        drawer.querySelector('.patient-age').textContent = card.dataset.patientAge;
        drawer.querySelector('.patient-condition').textContent = card.dataset.patientCondition;
        drawer.querySelector('.provider-name').textContent = card.dataset.providerName;
        drawer.querySelector('.appt-time').textContent = card.dataset.time;
        drawer.querySelector('.appt-duration').textContent = card.dataset.duration;
        drawer.querySelector('.appt-status').textContent = card.dataset.status;
        drawer.querySelector('.appt-type').textContent = card.dataset.type;

        drawer.classList.toggle('hidden');
    });
});

drawerClose.addEventListener('click', () => {
    drawer.classList.add('hidden');
});