document.addEventListener("DOMContentLoaded", async function () {
  const updateViewCount = async (method) => {
    try {
      const response = await fetch(
        `https://rcfa-che0dscycjh0fxar.canadacentral-01.azurewebsites.net/api/VisitCounter`,
        {
          method: method,
        }
      );
      const data = await response.text();
      return data; // Return the response data
    } catch (error) {
      console.error("Failed to update or retrieve view count", error);
      return null; // Return null in case of an error
    }
  };

  // Update the view count and then update the text on the webpage
  await updateViewCount("POST");
  const count = await updateViewCount("GET");

  // Use the retrieved count to update the text on the webpage
  const visitorCount = count ? count.toString().padStart(4, "0") : "0000";
  const viewCountElement = document.getElementById("view-count");
  if (viewCountElement) {
    viewCountElement.textContent = visitorCount;
  }
});