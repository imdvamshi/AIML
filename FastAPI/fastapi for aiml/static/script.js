async function PredictPrice(){
    const data = {
        area : parseFloat(document.getElementById("area").value),
        bedrooms : parseInt(document.getElementById("bedrooms").value),
        bathrooms : parseInt(document.getElementById("bathrooms").value)
    };
    const response = await fetch("http://127.0.0.1:8000/predict",{
        method : "POST", headers : {'content-type':'application/json'},body:JSON.stringify(data)
    });
    const result = await response.json();
    document.getElementById('result').innerHTML = "predicted price : ₹ " + result.prediction;
}