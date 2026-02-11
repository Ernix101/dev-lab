// 1. Outer Functions (Reusable Logic)
// Define here for broad use
function updateParagraphAndElementsText() {
  /*...*/
}
function applyCSS() {
  /*...*/
}
function renameInput() {
  /*....*/
}
function deleteFiles() {
  /*...*/
}
function MakeGlobalPromise() {
  /*...*/
}
function MakeAnAlert() {
  /*....*/
}
//
//
//
//
// 2. Arrays (Lists of Data)
// Use for collections  of similar items in one line as opposed to retyping const or similar items
const paragraphManager = [
  /*.....*/
];
const Names_Or_Numbers = [
  /*....*/
];
const cities = [
  /*.....*/
];
const references = [
  /*...getElementById1,QuerySelectorAll2,object1,object2...*/
];
const productObjects_And_Numbers = [
  /*...product1, product3...*/
];
//
//
//
//
// 3. Objects (Grouped Data and Methods)
// Use for bundling related data and actions
const objectName = {
  attribute_info: something_specific,
  elements_ForTheObject: paragraphs_headings,
  delays_ForTheObject: 3000, //these are milliseconds
  UpdateAll_ForTheObject: function () {
    this.elements.forEach((object) => {
      paragraphs.style.backgroundColor = "some color";
      h1.textcontent = "some text";
    });
  },
};
ResetAll: function name() {
  // Loop Example: for loop to reset
  for (let i = 0; i < this.elements.length; i++) {
    this.elements[i].textcontent = "some text";
    this.elements[i].style.backgroundColor = "white";
  }
}
//
//
//
//
// 4. Asynchronous Section (Promises, Async/Await,Fetch...)
// Handle timing, delays, or external data here.
function delayAction(callback, delay) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      try {
        callback();
        resolve("action completed");
      } catch (error) {
        reject(error);
      }
    }, delay);
  });
}

async function handleDlayedUpdate() {
  try {
    elements.forEach((element) => (element.someAction = "some value"));
    await delayAction(
      () => paragraphManager.updateAll(),
      paragraphManager.delay);               //we're using paragraphs as an example
    //could add await fetch(...) here for API calls later
    //
    //Fetch example
     isLoading = true;
    paragraphs.forEach(p => p.textcontent = isLoading ? "Loading..." : p.textcontent)
     const response = await fetch("https://someAPI with json placeholder")
    const data = await response.json();
    await delayAction(() => paragraphManager.updateAll(),paragraphManager.delay)
    
   //SetInterval Example: Update every second for 3 ticks
    let tickcount = 0;
      const intervalID = setInterval(() => {
        paragraphs.forEach(p.textcontent += ` - Tick ${++tickcount}`);
        if (tickcount === 3) clearInterval(intervalID);  //stop after 3
        }, 1000);
        isLoading = false; // update state
} catch (error) {
  paragraphs.forEach(p ,()=> p.textcontent = "Error" + error.message)
  
//0r....
  } catch (error) {
    paragraphs.forEach((p.textcontent = "some text as an example"));
  }
}
//
//
//
//
// 5. Event Listeners (Interactions)
// Attach with arrow functions to trigger logic
const button = document.getElementById("myBtn");
const my_prompt = document.getElementById("prompt"); //And any other interactive element

button.addEventListener("click", () => handleDlayedUpdate());

// 6. Future sections (eg. Event Emitters, Classes)
// Add as your projects evolve
