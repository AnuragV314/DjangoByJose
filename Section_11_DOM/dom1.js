let url = document.URL
console.log(url)

let body = document.body
console.log(body)

let head = document.head
console.log(head)

let links = document.links
console.log(links)



let pickme = document.getElementById("pickme").innerHTML
console.log(pickme)

let myul = document.getElementsByClassName("myul")
console.log(myul)

let tags = document.getElementsByTagName("li")
console.log(tags)


let query = document.querySelector("#pickme").innerHTML
console.log(query)

let queryall = document.querySelectorAll("li")
console.log(queryall)

let queryall2 = document.querySelectorAll(".myul")
console.log(queryall2)



// cahnging header color
var myheader = document.querySelector("h1")
console.log(myheader)


// myheader.style.color = 'red'

function getRandomColor(){
    var letters = "0123456789ABCDEF"
    var color = "#"
    for (var i=0; i<6; i++){
        color += letters[Math.floor(Math.random()*16)]
    }
    return color
}

function changeHeaderColor(){
    colorInput = getRandomColor()
    myheader.style.color = colorInput
}

setInterval("changeHeaderColor()", 500)
