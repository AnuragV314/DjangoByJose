// textContent
var p = document.querySelector('p')
p.textContent = "new text"
console.log(p)


// innerHTML
p.innerHTML = "<strong>I'm bold</strong>"
console.log(p)



var special = document.querySelector("#special")
console.log(special)

var specialA = special.querySelector("a")
console.log(specialA)

// getAttribute()
console.log(specialA.getAttribute("href"))


// setAttribute()
specialA.setAttribute("href", "http://www.amazon.com")
console.log(specialA.getAttribute("href"))
