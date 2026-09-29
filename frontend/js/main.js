const testButton = document.getElementById("testButton");
const apiResponse = document.getElementById("apiResponse");

testButton.addEventListener("click", async () => {
    try {
        const data = await get("/");
        apiResponse.textContent = data.message;
    } catch (error) {
        apiResponse.textContent = "Could not connect to API.";
        console.error(error);
    }
});