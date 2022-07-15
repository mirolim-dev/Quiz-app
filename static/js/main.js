console.log("Hello quiz");

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href
console.log('btns: ', modalBtns)
console.log('body: ', modalBody)

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{


    console.log(modalBtn)
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const questions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const pass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')
    
    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?
        <div class="text-muted">
            <ul>
                <li>Difficulty: <b>${difficulty}</b></li>
                <li>number of questions: <b>${questions}</b></li>
                <li>max ball: <b>${pass}</b></li>
                <li>duration time: <b>${time}</b></li>
            </ul>
        </div> 
        `

        startBtn.addEventListener('click', ()=>{
            window.location.href = url + 'test/' + pk
        })
}))




// console.log("Here quiz Js")
// const url = window.location.href
// console.log('url: ', url)

// $.ajax({
//     type: 'GET', 
//     url : `${url}test`
// })