document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      phone: document.getElementById("Phone").value,
      password: document.getElementById("password").value,
      role: "user"
    };

    try {
      const res = await fetch(`${API_BASE_URL}/users/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await res.json();

      if (!res.ok) {
        alert(result.detail || "Registration failed");
        return;
      }

      localStorage.setItem("user_id", result.id);
      window.location.href = "role.html";
    } catch (err) {
      alert("Backend not reachable");
      console.error(err);
    }
  });
});