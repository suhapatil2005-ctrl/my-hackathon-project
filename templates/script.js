async function predictScore() {

    const gender = document.getElementById("gender").value;
    const math = document.getElementById("math").value;
    const reading = document.getElementById("reading").value;

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            gender: gender,
            math: math,
            reading: reading
        })
    });
    const data = await response.json();

    document.getElementById("result").innerHTML = `
        Predicted Writing Score: <br><br>
        <strong>${data.prediction}</strong>
    `;
}