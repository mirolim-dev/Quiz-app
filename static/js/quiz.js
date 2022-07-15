// console.log("Here quiz Js")
// const url = window.location.href
// console.log('url: ', url)\
const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const elements = [...document.getElementsByClassName('ans')]
const time = quizForm.getAttribute('data-time')


const url = window.window.location.href

const timerBox = document.getElementById('timer-box')

const activateTimer = (time) =>{
    console.log(time)

    if (time.toString().length < 2){
        timerBox.innerHTML = `<b>0${time}:00</b>`
    }
    else{
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time-1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds<0){
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2){
            displayMinutes = '0'+minutes
        }
        else{
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2){
            displaySeconds = '0'+seconds
        }
        else{
            displaySeconds = seconds
        }
        if (minutes===0 && seconds===0){
            console.log("Time is Up")
            clearInterval(timer)
            alert("Time is Up")
            sendData()
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}


$.ajax({
    type: 'GET', 
    url : url,
    success: function(response){
        console.log("Ajax ishlayabdi")
        if (time > 0){
            activateTimer(time)
            }   
    },
    error: function(error){
        console.log(error)
    }
})


const sendData = () => {
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked){
            data[el.name] = el.value
        }
        else{
            if (!data[el.name]){
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type: 'POST',
        url: `${url}save`,
        data: data,
        success: function(response){
            console.log('quiz ajax respons from request Post',response)
        },
        error: function(error){
            console.log('error: ', error)
        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})