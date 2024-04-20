window.onload = (event) => {
    console.log("page is fully loaded");
    const userSelect = document.getElementById("user-select");
    const profileInfoDiv = document.getElementById("profile-info"); // Define userSelect variable

    // Add event listener to detect when a user is selected
    userSelect.addEventListener('change', (event) => {
      
        const selectedUserName = event.target.value;
        fetchUserProfile(selectedUserName);
        
        
    });

    // Fetch user profiles and populate dropdown
    fetch('http://3.15.174.171:8000/api/v1/userprofiles/')
        .then(response => response.json())
        .then(data => {
            // Populate dropdown with user names
            data.forEach(userProfile => {
                const userName = userProfile.account.first_name + " " + userProfile.account.last_name;
                const option = document.createElement('option');
                option.value = userName;
                option.textContent = userName;
                userSelect.appendChild(option);
                
            });
        })
        .catch(error => {
            console.error('Error fetching user profiles:', error);
        });

    // Function to fetch profile information and advertisements for the selected user
// Function to fetch profile information and advertisements for the selected user
function fetchUserProfile(userName) {
    // Make a fetch request to get the profile info for the selected user
    fetch('http://3.15.174.171:8000/api/v1/userprofiles/')
        .then(response => response.json())
        .then(userProfiles => {
            // Find the user profile data for the selected user
            const userProfile = userProfiles.find(user => user.account.first_name + " " + user.account.last_name === userName);
            if (userProfile) {
               
                // Display profile information
                displayProfileInfo(userProfile);
                
                
                // Fetch advertisements for the selected user
                fetch('http://3.15.174.171:8000/api/v1/advertisements/')
                    .then(response => response.json())
                    .then(advertisements => {
                        // Filter advertisements for the selected user
                        const userAdvertisements = advertisements.filter(advertisement => advertisement.seller_account_id.first_name + " " + advertisement.seller_account_id.last_name === userName);
                        // Display advertisement information
                        if (userAdvertisements.length > 0) {
                            // Display the first advertisement found
                            const advertisementContent = `
                                <strong>Advertisement Date:</strong> ${userAdvertisements[0].advertisement_date}<br><br>
                                <strong>Car Make:</strong> ${userAdvertisements[0].car_id.car_model_id.make}<br><br>
                                <strong>Car Model:</strong> ${userAdvertisements[0].car_id.car_model_id.model}<br><br>
                                <strong>Registration Number:</strong> ${userAdvertisements[0].car_id.registration_number}<br><br>
                                <strong>Manufacture Year:</strong> ${userAdvertisements[0].car_id.manufacture_year}<br><br>
                                <strong>Number of Doors:</strong> ${userAdvertisements[0].car_id.number_of_doors}<br><br>
                                <strong>Mileage:</strong> ${userAdvertisements[0].car_id.mileage}
                            `;
                            displayAdvertisement(advertisementContent);
                        } else {
                            console.log('No advertisements found for the user.');
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching advertisements:', error);
                    });
            } else {
                console.error('Profile not found for user:', userName);
            }
        })
        .catch(error => {
            console.error('Error fetching user profiles:', error);
        });
}


       // Function to display profile information
       function displayProfileInfo(userProfile) {
        const profileInfoDiv = document.getElementById("profile-info");
        profileInfoDiv.innerHTML = ''; // Clear previous profile info
    
        // Create elements to display profile info
        const profileHeader = document.createElement('h2');
        profileHeader.textContent = 'User Profile:';
        
        const nameParagraph = document.createElement('p');
        nameParagraph.textContent = `Name: ${userProfile.account.first_name} ${userProfile.account.last_name}`;
    
        const emailParagraph = document.createElement('p');
        emailParagraph.textContent = `Email: ${userProfile.account.email}`;
    
        const addressParagraph = document.createElement('p');
        addressParagraph.textContent = `Address: ${userProfile.street_number} ${userProfile.street_name}, ${userProfile.zip_code} ${userProfile.city}`;
    
        // Add profile info elements to the div
        profileInfoDiv.appendChild(profileHeader);
        profileInfoDiv.appendChild(nameParagraph);
        profileInfoDiv.appendChild(emailParagraph);
        profileInfoDiv.appendChild(addressParagraph);
      
    }
        // Fetch advertisemts profiles and populate dropdown
        fetch('http://3.15.174.171:8000/api/v1/advertisements/')
        .then(response => response.json())
        .then(data => {
            // Populate dropdown with user names
            console.log(data)
            
        })
        .catch(error => {
            console.error('Error fetching user profiles:', error);
        });

        // Fetch user profiles and populate dropdown
        fetch('http://3.15.174.171:8000/api/v1/cars/')
        .then(response => response.json())
        .then(data => {
            // Populate dropdown with user names
            console.log(data)
            
        })
        .catch(error => {
            console.error('Error fetching user profiles:', error);
        });

// Function to display advertisement information
function displayAdvertisement(advertisement) {
    const advertisementInfoDiv = document.getElementById("advertisement-info");
    advertisementInfoDiv.innerHTML = ''; // Clear previous advertisement info

    // Create elements to display advertisement info
    const advertisementHeader = document.createElement('h2');
    advertisementHeader.textContent = 'Advertisement:';

    const advertisementParagraph = document.createElement('p');
    advertisementParagraph.innerHTML = advertisement;

    // Add advertisement info elements to the div
    advertisementInfoDiv.appendChild(advertisementHeader);
    advertisementInfoDiv.appendChild(advertisementParagraph);
    // Add other advertisement fields as needed
}
   
}


  // <strong>Seller Name:</strong> ${userAdvertisements[0].seller_account_id.first_name} ${userAdvertisements[0].seller_account_id.last_name}<br><br>
                                // <strong>Email:</strong> ${userAdvertisements[0].seller_account_id.email}<br><br>