const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.nav__link')
const requestCV = document.querySelector('.btn-stats') 
const closeStats = document.getElementById('stats-close-id')


navToggle.addEventListener('click', () => {
    document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    })
})

// requestCV.addEventListener('click', () => {
//     document.body.classList.toggle('stats-open');
// });

// closeStats.addEventListener('click', () => {
//     document.body.classList.remove('stats-open')
// })


// let emailCollectorForm = document.getElementById('Email-Form')
// console.log(emailCollectorForm)
// emailCollectorForm.addEventListener("submit", event => {
//     event.preventDefault()

//     let ourFormData = new FormData(event.target)
//     let userFirstName = ourFormData.get("firstName")
//     let userEmailAddress = ourFormData.get("emailAddress")

//     let updateContentHTML = `
//         <h2 class="section__title">Congratulations, ${userFirstName}!</h2>
//         <p>You're on your way to becoming a BBQ Master!</p>
//         <p class="fine-print">Ahsan will shortly notify you to: ${userEmailAddress}</p>
//     `
//     let mainContent = document.getElementById("contact") 
//     mainContent.innerHTML = updateContentHTML
// })