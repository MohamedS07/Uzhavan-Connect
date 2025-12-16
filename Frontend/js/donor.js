document.getElementById("donorform").addEventListener("submit", async function (e) {
  e.preventDefault();

  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Please login first");
    return;
  }

  const name = document.querySelector('input[placeholder="Enter your Name"]').value;
  const state = document.getElementById("state").value;
  const email = document.querySelector('input[placeholder="Enter your Address"]').value;
  const phone = document.querySelector('input[placeholder="Enter your Phone Number"]').value;

  const occupationType = document.querySelector('input[name="apply_type"]:checked')?.value || null;
  const occupationName = document.querySelector('input[placeholder="Occupation / Organization"]').value;

  const payload = {
    user_id: parseInt(userId),
    name: name,
    state: state,
    email: email,
    phone: phone,
    occupation_type: occupationType,
    occupation_name: occupationName
  };

  try {
    const res = await fetch(`${API_BASE_URL}/donors/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed");

    alert("✅ Donor registered successfully");
    document.getElementById("donorForm").reset();

  } catch (err) {
    alert("❌ Error registering donor");
    console.error(err);
  }
});
