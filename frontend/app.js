const functionUrl = "https://rcfa-che0dscycjh0fxar.canadacentral-01.azurewebsites.net/api/VisitCounter";

async function incrementVisitorCount() {
  try {
    const res = await fetch(functionUrl, { method: "POST" });
    if (!res.ok) throw new Error(res.status);
    const data = await res.json();
    document.getElementById("visitors").textContent = data.count;
  } catch (e) {
    console.error("Visitor counter error:", e);
    document.getElementById("visitors").textContent = "error";
  }
}
window.addEventListener("DOMContentLoaded", incrementVisitorCount);
