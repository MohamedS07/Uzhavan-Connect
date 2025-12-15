document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  formData.append("user_id", localStorage.getItem("user_id"));

  const res = await fetch("http://127.0.0.1:8000/farmers/", {
    method: "POST",
    body: formData
  });

  if (res.ok) {
    alert("Farmer registered successfully");
  } else {
    alert("Error");
  }
});

