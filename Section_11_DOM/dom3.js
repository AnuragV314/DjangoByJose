var headOne = document.querySelector("#one")
var headTwo = document.querySelector("#two")
var headThree = document.querySelector("#three")

console.log("connected!")

// mouseover
headOne.addEventListener("mouseover", function(){
    headOne.textContent = "Mouse Currently Over";
    headOne.style.color = "red"
})

// mouseout
headOne.addEventListener("mouseout", function(){
    headOne.textContent = "Hover Over Me!"
    headOne.style.color = "black"
})



headTwo.addEventListener("mouseover", function(){
    headTwo.style.cursor = "pointer"
})
// click
headTwo.addEventListener("click", function(){
    headTwo.textContent = "Clicked on"
    headTwo.style.color = "blue"
})



headThree.addEventListener("mouseover", function(){
    headThree.style.cursor = "pointer"
})
// dblclick
headThree.addEventListener("dblclick", function(){
    headThree.textContent = "Double Clicked"
    headThree.style.color = "red"
})

