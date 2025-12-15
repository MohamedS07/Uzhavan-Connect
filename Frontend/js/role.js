const userId = localStorage.getItem("user_id");

function selectRole(role) {
  fetch(`http://127.0.0.1:8000/users/${userId}/role`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ role })
  })
  .then(res => res.json())
  .then(() => {
    localStorage.setItem("role", role);

    if (role === "farmer") window.location.href = "farmer.html";
    if (role === "donor") window.location.href = "donor.html";
    if (role === "ngo") window.location.href = "ngo.html";
  });
}

