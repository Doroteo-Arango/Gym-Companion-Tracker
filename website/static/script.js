// Delete notes
function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res) => {
        // Reload window with get request
        window.location.href = '/';
    });
}

// BMI Calculator
function calculate(height, weight) {
    weight = parseInt(weight);
    height = parseInt(height);
    console.log("Height", height);
    console.log("Weight", weight);
    weight = weight * 703;
    height = height*height;
    var bmi = weight/height;
    console.log("BMI: ", bmi);
    document.getElementById('bmi').innerHTML = bmi.toPrecision(3);
    
    if(bmi < 18.5)
      {
        document.getElementById('range').innerHTML = "Underweight";
        document.getElementById('range').classList.remove("neutral");
        document.getElementById('range').classList.remove("good");                 document.getElementById('range').classList.add("bad");
      }
    
     if(bmi >= 18.5 && bmi < 25)
      {
        document.getElementById('range').innerHTML = "Normal";
        document.getElementById('range').classList.remove("neutral");
        document.getElementById('range').classList.remove("bad");                   document.getElementById('range').classList.add("good");
      }
    
     if(bmi >= 25 && bmi < 30)
      {
        document.getElementById('range').innerHTML = "Overweight";
        document.getElementById('range').classList.remove("neutral");
        document.getElementById('range').classList.remove("good");                 document.getElementById('range').classList.add("bad");
      }
    
     if(bmi > 30)
      {
        document.getElementById('range').innerHTML = "Obese";
        document.getElementById('range').classList.remove("neutral");
        document.getElementById('range').classList.remove("good");                 document.getElementById('range').classList.add("bad");
      }
  };
  
  function clear_calculator(){
    console.log("Clear");
    document.getElementById('range').classList.remove("bad");
    document.getElementById('range').classList.remove("good");
    document.getElementById('range').classList.add("neutral");
    document.getElementById('range').innerHTML = "Enter Measurements";
    document.getElementById('bmi').innerHTML = "--.--";
    document.getElementById('height_input').value="";
    document.getElementById('weight_input').value="";
    document.getElementById('height_input').focus();
  };
