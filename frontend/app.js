document.addEventListener('DOMContentLoaded', () => {
    const visitorsDiv = document.getElementById('visitors');
    
    // Function to increment visitor count
    const incrementVisitorCount = async () => {
        try {
            // POST request to the API
            const postResponse = await fetch('https://rcfa-che0dscycjh0fxar.canadacentral-01.azurewebsites.net/api/VisitCounter', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            });

            // Check if the request was successful
            if (!postResponse.ok) {
                throw new Error('Network response was not ok');
            }

            // Fetch the JSON result
            const jsonResponse = await postResponse.json();

            // Display the new_count in the visitors div
            visitorsDiv.innerText = `Visitor count incremented. New count: ${jsonResponse.new_count}`;
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            visitorsDiv.innerText = 'Error incrementing visitor count.';
        }
    };

    incrementVisitorCount();
});
