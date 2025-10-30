document.getElementById("predictBtn").addEventListener("click", async () => {
  const ph = document.getElementById("phInput").value;
  if (!ph) {
    alert("Please enter a pH value!");
    return;
  }

  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ph: ph }),
  });

  const data = await response.json();

  if (data.error) {
    document.getElementById("result").innerHTML = "⚠️ Error: " + data.error;
  } else {
    document.getElementById("result").innerHTML = `
      💧 Water Quality: <b>${data.prediction}</b><br>
      Bad: ${data.probabilities.Bad}%<br>
      Average: ${data.probabilities.Average}%<br>
      Good: ${data.probabilities.Good}%
    `;
  }
});
