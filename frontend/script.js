async function validate() {

  const data = {
    thickness: parseFloat(document.getElementById("thickness").value),
    hole_diameter: parseFloat(document.getElementById("hole").value),
    width: parseFloat(document.getElementById("width").value)
  };

  const res = await fetch("http://127.0.0.1:5000/validate", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });

  const result = await res.json();

  document.getElementById("result").innerHTML = `
    <h2>Validation Report</h2>

    <h3>Score: ${result.score}/10</h3>
    <div style="background:#334155; border-radius:10px; overflow:hidden;">
      <div style="width:${result.score * 10}%; background:#22c55e; height:10px;"></div>
    </div>

    <p style="color:#ef4444;"><b>Errors:</b> ${result.errors.join(", ") || "None"}</p>
    <p style="color:#facc15;"><b>Warnings:</b> ${result.warnings.join(", ") || "None"}</p>
    <p style="color:#22c55e;"><b>Suggestions:</b> ${result.suggestions.join(", ") || "None"}</p>
  `;
}