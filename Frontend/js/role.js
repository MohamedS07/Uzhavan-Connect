const API = "http://127.0.0.1:8000";
const userId = localStorage.getItem("user_id");

if (!userId) {
  alert("Login first");
  window.location.href = "sign-up.html";
}

async function setRole(role, redirect) {
  try {
    const res = await fetch(`${API}/users/${userId}/role`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ role })
    });

    if (!res.ok) {
      const err = await res.json();
      alert(err.detail || "Role update failed");
      return;
    }

    window.location.href = redirect;
  } catch (e) {
    alert("Backend error");
    console.error(e);
  }
}

document.getElementById("farmerBtn").addEventListener("click", () =>
  setRole("farmer", "farmer.html")
);

document.getElementById("donorBtn").addEventListener("click", () =>
  setRole("donor", "donor.html")
);

document.getElementById("ngoBtn").addEventListener("click", () =>
  setRole("ngo", "ngo.html")
);
