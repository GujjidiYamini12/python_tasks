setTimeout(() => {
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach((alert) => {
        alert.style.transition = "opacity 0.4s";
        alert.style.opacity = "0";
    });
}, 2500);
