document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registerForm");

  if (!form) {
    console.error("❌ Register form not found");
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault(); // 🔥 VERY IMPORTANT

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
      const res = await fetch(`${API_BASE_URL}/users/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: email,
          password: password,
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        alert(data.detail || "Registration failed");
        return;
      }

      // ✅ SAVE USER ID
      localStorage.setItem("user_id", data.id);

      // ✅ REDIRECT
      window.location.href = "role.html";

    } catch (err) {
      console.error("❌ Backend not reachable", err);
      alert("Backend not reachable");
    }
  });
});
