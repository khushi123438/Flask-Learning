
const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    message.textContent = "Logging in...";

    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        message.textContent = data.message;
        message.style.color = data.success ? "green" : "red";

        if (data.success) {
            console.log("Login successful");
        }
    } catch (error) {
        message.textContent = "Server se connect nahi ho pa raha.";
        message.style.color = "red";
    }
});
