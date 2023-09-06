// method 1 

// var carInfo = {make:"toyota", year:1990, model:"Camry"};
// console.log(carInfo)
// console.log(carInfo["make"])


// method 2

// var carInfo = new Object() // create an onject carInfo

// carInfo.make = "toyota"
// carInfo.year = 1990
// carInfo.model = "Camry"

// console.log(carInfo)
// console.log(carInfo["make"])


// for (key in carInfo){
//     console.log(key,carInfo[key])
// }



// making function inside the objects
// this keyword ===> 

// var carInfo = {
//     make:"toyota", 
//     year:1990, 
//     model:"Camry",

//     car:function(){
//         return this.make + this.year + this.model;
//     }
// };

// console.log(carInfo)
// console.log(carInfo["make"])
// console.log(carInfo.car())



var name_ = "anurag Verma".split(" ")
console.log(name_)
console.log(name_[1])


