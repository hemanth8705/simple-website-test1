// Define a Function
function sayOuch() {
	alert('Hey, you just clicked the logo!');
}

// Use a CSS selector to identify an element
var logo = document.querySelector('img');

// Assign the function to the onclick event on that element
logo.onclick = sayOuch;

// Fetch the JSON data
fetch('data.json')
    .then(response => response.json())
    .then(data => {
        // Set the content dynamically
        document.getElementById('heading').innerText = data.heading;
        document.getElementById('subheading').innerText = data.subheading;
        document.getElementById('paragraph1').innerText = data.paragraph1;
        document.getElementById('paragraph2').innerText = data.paragraph2;

        // Populate the bullet points
        const ul = document.getElementById('bulletPoints');
        data.bulletPoints.forEach(point => {
            const li = document.createElement('li');
            li.textContent = point;
            ul.appendChild(li);
        });
    })
    .catch(error => console.error('Error loading data:', error));
