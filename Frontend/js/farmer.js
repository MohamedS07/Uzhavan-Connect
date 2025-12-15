document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    try {
      const res = await fetch(`${API_BASE_URL}/farmers/`, {
        method: "POST",
        body: formData
      });

      const result = await res.json();

      if (!res.ok) {
        alert("Farmer registration failed");
        return;
      }

      alert("Farmer registered successfully");
      form.reset();
    } catch (err) {
      alert("Backend error");
      console.error(err);
    }
  });
});
