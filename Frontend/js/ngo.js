document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: document.getElementById("name").value,
      registration_number: document.getElementById("reg_no").value,
      email: document.getElementById("email").value,
      phone: document.getElementById("phone").value
    };

    try {
      const res = await fetch(`${API_BASE_URL}/ngos/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      if (!res.ok) {
        alert("NGO registration failed");
        return;
      }

      alert("NGO registered successfully");
      form.reset();
    } catch (err) {
      alert("Backend error");
      console.error(err);
    }
  });
});
