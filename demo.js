let a = {
    name: "shiddhe",
    roll_no: 62,
    marks: "FAIL",
    
    get: function(){
        console.log("Name: ",this.name , "\nRoll no: ",this.roll_no, "\nMarks: ", this.marks);        
    }
}

a.get();