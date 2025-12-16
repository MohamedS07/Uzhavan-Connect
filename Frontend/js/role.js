document.addEventListener("DOMContentLoaded", () => {
  const userId = localStorage.getItem("user_id");

  console.log("User ID:", userId);

  if (!userId) {
    alert("Please register first");
    window.location.href = "sign-up.html";
    return;
  }

  async function setRole(role, redirectPage) {
    try {
      const res = await fetch(`${API}/users/${userId}/role`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ role })
      });

      if (!res.ok) {
        const err = await res.json();
        console.error(err);
        alert("Role update failed");
        return;
      }

      console.log("Role updated:", role);
      window.location.href = redirectPage;

    } catch (error) {
      console.error("Network error", error);
      alert("Backend not reachable");
    }
  }

  document.getElementById("farmerBtn").onclick = () =>
    setRole("farmer", "farmer.html");

  document.getElementById("donorBtn").onclick = () =>
    setRole("donor", "donor.html");

  document.getElementById("ngoBtn").onclick = () =>
    setRole("ngo", "ngo.html");
});
