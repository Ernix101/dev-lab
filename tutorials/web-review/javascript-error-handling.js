// Error = An object that is created to represent a problem that occurs
//          They occur often with user input or establishing a connection

//   NETWORK ISSUES
//  PROMISE REJECTION
//  SECURITY ERRORS 

// There is a solution. and that is to surround that with:
//  try { } = Encloses the code that might potentially cause an error
//  catch { } = Catch and handle any thrown errors from try { }
//  finally { } = (optional) Always executes. Used mostly for clean up
//                  eg: close files, close connections, release resources


try{
    const dividend = Number(window.prompt("Enter a dividend: "));
    const divisor = Number(window.prompt("Enter a divisor: "));

    if(divisor == 0){
        throw new Error("You can't divide by zero!")
    }
    if(isNaN(dividend) || isNaN(divisor)){
        throw new Error("Value must be a number");
    }

    const result = dividend / divisor
    console.log(result);
}
catch(error){
    console.error(error)
}
console.log("You have reached the end!");












































// try {
//     console.log("Hello");
// }
// catch(error){
//     console.error(error);
// }
// finally{
//     console.log("This always executes")
// }

// console.log("You have reached the end!");
