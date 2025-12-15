const userId = localStorage.getItem("user_id");

if (!userId) {
  alert("User not found. Please register again.");
}

async function updateRole(role, redirectPage) {
  try {
    const res = await fetch(`${API_BASE_URL}/users/${userId}/role`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ role })
    });

    if (!res.ok) {
      const data = await res.json();
      alert(data.detail || "Role update failed");
      return;
    }

    window.location.href = redirectPage;
  } catch (err) {
    alert("Backend error");
    console.error(err);
  }
}
