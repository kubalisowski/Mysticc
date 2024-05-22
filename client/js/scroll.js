//https://dev.to/ak_ram/asynchronous-javascript-operations-understanding-canceling-pausing-and-resuming-4ih5

var run_scroll = false

$(function() { 
    while (run_scroll) {
        console.log(1)
    }
})


function startScroll() {
    run_scroll = true
}

function stopScroll() {
    run_scroll = false
}

$('#up_scroll').mouseover(function () {
    startScroll()
})

$('#up_scroll').mouseout(function () {
    stopScroll()
})

// var timeoutRefs = [];

// function sleep(ms) {
//   return new Promise(resolve => timeoutRefs.push(setTimeout(resolve, ms)));
// }

// $('#up_scroll').mouseover(function () {
//     sleep(250).then(() => { console.log(1) })
// })

// $('#up_scroll').mouseout(function () {
//     timeoutRefs.forEach(function (timeoutRef) {
//         clearTimeout(timeoutRef)
//     })
//     timeoutRefs = []
//     console.log(2)
// })


