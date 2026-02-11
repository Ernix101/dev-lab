const students = [
    { id: 1, name: "Alice", score: 85, region: "Nairobi" },
    { id: 2, name: "Brian", score: 67, region: "Kisumu" },
    { id: 3, name: "cynthia", score: 45, region: "Nairobi" },
    { id: 4, name: "David", score: 90, region: "Mombasa" },
    { id: 5, name: "Eva", score: 72, region: "Kisumu" },
    { id: 6, name: "Frank", score: 55, region: "Nairobi" },
    { id: 7, name: "Grace", score: 38, region: "Eldoret" }
]

const studentName = students.map((student) => {
    return student.name
})

// console.log(studentName);

const increasedScorebyOne = students.map( (student) => {
    return student.score + 1
})

// console.log(increasedScorebyOne)




const highGrade = students.filter((student) => {
    if(student.score > 50) {
        return student.score
    }
})
    
// console.log(highGrade);

const studentsFromNairobi = students.filter(student => student.region === "Nairobi");

// console.log(studentsFromNairobi);




const totalScore = students.reduce((total, student) => {
    return total + student.score
},0)

// console.log(totalScore);

const averageScore = students.reduce(() => {
    return totalScore / students.length
})
// console.log(averageScore);




const IsBelowForty = students.some(student => student.score < 40);

// console.log(IsBelowForty);  // returns true or false, but what if we wanted the number

const IsMombasaStudent = students.some(student => student.region === "Mombasa");
// console.log(IsMombasaStudent);





const numBelowForty = students.filter(student => student.score < 40);
// console.log(numBelowForty.length);  // now we know how many


const findAboveEighty = students.find(student => student.score > 80);

// console.log(findAboveEighty.name); returns names of scorers above 80

const findEva = students.find(student => student.name === "Eva");

// console.log(findEva);





const summary = students.reduce((acc, student) => {
    // Total count of students
    acc.totalStudents++;

    // Check pass or fail
    if(student.score >= 50){
        acc.passed++;
    } else {
        acc.failed++;
    }

    //check for top scorer
    if(student.score > acc.topScorer.score){
        acc.topScorer = student; // keep whole student object
    }
    return acc;
}, {
    totalStudents: 0,
    passed: 0,
    failed: 0,
    topScorer: { name: "", score: 0}
});

console.log(summary);


class Student{
    constructor(name, grade){
        this.name = name,
        this.grade = grade
    }

    displayDetails(){
        console.log(`${this.name} has scored ${this.grade}`)
    }
    isPass(){
        if(this.grade >= 50) {
            return "Pass"
        }else{
            return "Fail"
        }
    }
    UpdateGrade(NewGrade){
        return this.grade = NewGrade
    }
}

let studentsB = [
    new Student("Alice", 80),
    new Student("Bob", 45),
    new Student("Brian", 67),
    new Student("David", 90)
];



// console.log(Bob.isPass());
// console.log(Alice.isPass());
// Alice.UpdateGrade(92);
// console.log(Alice.grade);

studentsB.forEach(student => {
    console.log(student.name, "-->", student.isPass());
})



