// var num = [1,4,3,6]
// console.log(num[2])
// num[2]=10
// console.log(num[2])



// // immutable
// var emp = ["A", "B", "C"]
// console.log(emp[0])
// emp[0] = "D"
// console.log(emp[0])

// // mutable
// var a = "Anurag"
// console.log(a[0])
// a[0] = "B"
// console.log(a[0])




// foreach() method

// function addAwesom(name){
//     console.log(name + " is awesome!")
// }

// var topics = ["python", "django", "nodejs"]

// topics.forEach(addAwesom)



var roster = []

function addNew(){
    var newName = prompt("What name would you like to add?")
    roster.push(newName)
}

function remove(){
    var remName = prompt("What name would you like to remove?")
    var index = roster.indexOf(remName)
    roster.splice(index, 1)
}

function display(){
    console.log(roster)
}


var start = prompt("would you like to start the roster web app?y/n")
var request = "empty"


if (start==='y') {
    while (request !== "quit") {
        request = prompt("Please select an action: add, remove, display or quit.")

        if (request === "add") {
            addNew()
        }
        else if(request === "display"){
            display()
        }
        else if(request === "remove"){
            remove()
        }
        else{
            request = "quit"
        }

        alert("Thanks for using the Web App.")

    }
}

