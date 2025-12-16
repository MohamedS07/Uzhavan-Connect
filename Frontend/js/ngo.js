document.getElementById("ngoform").addEventListener("submit", async function (e) {
  e.preventDefault();

  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Please login first");
    return;
  }

  const name = document.querySelector('input[placeholder="Enter NGO Name"]').value;
  const registrationNumber = document.querySelector('input[placeholder="Enter NGO Registration Number"]').value;
  const district = document.querySelector(".district").value;
  const contactPerson = document.querySelector('input[placeholder="NGO Contact Person"]').value;
  const phone = document.querySelector('input[placeholder="Enter Contact Number"]').value;
  const email = document.querySelector('input[placeholder="Enter Email"]').value;

  const payload = {
    user_id: parseInt(userId),
    name: name,
    registration_number: registrationNumber,
    district: district,
    contact_person: contactPerson,
    phone: phone,
    email: email
  };

  try {
    const res = await fetch(`${API_BASE_URL}/ngos/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed");

    alert("✅ NGO registered successfully");
    document.getElementById("ngoForm").reset();

  } catch (err) {
    alert("❌ Error registering NGO");
    console.error(err);
  }
});
