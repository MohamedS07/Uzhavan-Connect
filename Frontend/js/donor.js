document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      phone: document.getElementById("phone").value,
      amount: document.getElementById("amount").value
    };

    try {
      const res = await fetch(`${API_BASE_URL}/donors/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      if (!res.ok) {
        alert("Donor registration failed");
        return;
      }

      alert("Donor registered successfully");
      form.reset();
    } catch (err) {
      alert("Backend error");
      console.error(err);
    }
  });
});
