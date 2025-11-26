// Show image preview
document.getElementById("upload").addEventListener("change", function(event){
    const img = document.getElementById("image-preview");
    img.src = URL.createObjectURL(event.target.files[0]);
    img.style.display = "block";
});

async function estimateCalorie() {
    const fileInput = document.getElementById("upload");
    const resultBox = document.getElementById("result-box");

    if (!fileInput.files[0]) {
        resultBox.innerHTML = "Please upload an image first.";
        return;
    }

    resultBox.innerHTML = "Predicting... ⏳";

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        resultBox.innerHTML = `
            🍇 Detected: <b>${data.label}</b><br>
            🔥 Calories per 100g: <b>${data.calories}</b>
        `;
    } catch (error) {
        resultBox.innerHTML = "❌ Error contacting server.";
    }
}