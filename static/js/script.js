const machineryBtn = document.getElementById("machinery-btn");
const rentalBtn = document.getElementById("rental-btn");
const purchaseBtn = document.getElementById("purchase-btn");
const optionsDiv = document.querySelector(".machinery-options");

function showMachineryOptions() {
    const machineryContainer = document.querySelector(".machinery-container");
    machineryContainer.classList.toggle("active");
}

machineryBtn.addEventListener("click", showMachineryOptions);

rentalBtn.addEventListener("click", () => {
    // Code to show machinery data for rental
});

purchaseBtn.addEventListener("click", () => {
    // Code to show machinery data for purchase
});



// remove profile info from HTML since we're now using the dropdown-content element
const profilePic = document.getElementById("profile-img");
const dropdown = document.querySelector(".dropdown");
const dropdownContent = document.querySelector(".dropdown-content");

profilePic.addEventListener("click", () => {
    dropdownContent.classList.toggle("active");
});

// hide dropdown when clicking outside of it
window.addEventListener("click", (e) => {
    if (!dropdown.contains(e.target)) {
        dropdownContent.classList.remove("active");
    }
});

