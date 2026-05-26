const revealItems = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14 }
  );

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

// Handle waitlist form submission
const waitlistForm = document.getElementById("waitlistForm");
const submitBtn = document.getElementById("submitBtn");
const formMessage = document.getElementById("formMessage");

if (waitlistForm) {
  waitlistForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Collect form data
    const formData = new FormData(waitlistForm);
    const data = Object.fromEntries(formData.entries());

    // Show loading state
    submitBtn.disabled = true;
    submitBtn.textContent = "Submitting...";

    try {
      const response = await fetch("http://localhost:5000/submit-waitlist", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (response.ok) {
        // Success
        formMessage.textContent = result.message || "Thank you! Your details have been submitted successfully.";
        formMessage.style.color = "green";
        waitlistForm.reset();
        submitBtn.textContent = "Submit Details";
        submitBtn.disabled = false;

        // Reset message after 5 seconds
        setTimeout(() => {
          formMessage.textContent = "Your submission will be sent to nwokoloebube21@gmail.com with the title 'EgoTrack Waitlist'.";
          formMessage.style.color = "";
        }, 5000);
      } else {
        // Error
        formMessage.textContent = result.error || "Failed to submit. Please try again.";
        formMessage.style.color = "red";
        submitBtn.textContent = "Submit Details";
        submitBtn.disabled = false;
      }
    } catch (error) {
      console.error("Error:", error);
      formMessage.textContent = "Server is not running. Please make sure the Flask server is started.";
      formMessage.style.color = "red";
      submitBtn.textContent = "Submit Details";
      submitBtn.disabled = false;
    }
  });
}

