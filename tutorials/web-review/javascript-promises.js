// Promise = An object that manages asynchronous operations.
//          Wrap a Promise object around (asynchronous code)
//          "I promise to return a value"
//          PENDING -> RESOLVED or REJECTED
//          new Promise((resolve, reject) => {asynchronous code})

// eg DO THESE CHORES IN ORDER

// 1. WALK DOG
// 2. CLEAN KITCHEN
// 3. TAKE OUT TRASH

function walkDog(){

    return new Promise((resolve, reject) => {
    setTimeout(() => {

        const dogWalked = true;

        if(dogWalked){
            resolve("You Walk the Dog");
        } else {
            reject("You DIDN'T walk the dog")
        }

    }, 1500)
    });
}

function cleanKitchen(){

    return new Promise((resolve, reject) => {
    setTimeout(() => {

        const kitchenCleaned = true;

        if(kitchenCleaned){
            resolve("You clean the kitchen");
        } else {
            reject("You DIDN'T clean the kitchen")
        }

    }, 2500)
    })
}

function takOutTrash(){

    return new Promise((resolve, reject) => {
    setTimeout(() => {

        const trashTakenOut = true;

        if(trashTakenOut){
            resolve("You take out the trash");
        } else {
            reject("You DIDN'T take out the trash");
        }
            
        }, 500)
    })
}


walkDog().then(value => {console.log(value); return cleanKitchen()})
         .then(value => {console.log(value); return takOutTrash()})
         .then(value => {console.log(value); console.log("You finished all the chores")})
         .catch(error => console.error(error));



// Here is how we can call the functions in order using callback hell
// walkDog(() => {
//     cleanKitchen(() => {
//         takOutTrash(() => {console.log("You finished all the chores")})
//     })
// })

//To avoid using callback hell. We'll wrap them inside a promise and use method chaining instead

