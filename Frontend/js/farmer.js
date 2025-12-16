const API = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("farmerForm");

  if (!form) {
    console.error("❌ Farmer form not found");
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault(); // 🔥 MUST

    console.log("✅ Apply button clicked");

    const formData = new FormData(form);

    try {
      const res = await fetch(`${API}/farmers/`, {
        method: "POST",
        body: formData
      });

      const data = await res.json();

      if (!res.ok) {
        console.error(data);
        alert(data.detail || "❌ Farmer registration failed");
        return;
      }

      alert("✅ Farmer registered successfully");

      // 👉 Dashboard redirect (example)
      window.location.href = "farmer-dashboard.html";

    } catch (err) {
      console.error("❌ Network error", err);
      alert("Server not reachable");
    }
  });
});
