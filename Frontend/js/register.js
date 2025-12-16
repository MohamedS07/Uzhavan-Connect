const API_BASE_URL = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      email: document.getElementById("email").value,
      password: document.getElementById("password").value,
      role: "user"   // default role
    };

    try {
      const res = await fetch(`${API_BASE_URL}/users/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });

      const result = await res.json();

      if (!res.ok) {
        alert(result.detail || "Registration failed");
        return;
      }

      // ✅ VERY IMPORTANT
      localStorage.setItem("user_id", result.id);

      // 👉 go to role selection page
      window.location.href = "role.html";

    } catch (err) {
      alert("Backend not reachable");
      console.error(err);
    }
  });
});
