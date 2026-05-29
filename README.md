index.html
<!DOCTYPE html>
<html>
<head>
    <title>Sai Tejaswi Portfolio</title>
</head>

<body>

    <h1>B. Sai Tejaswi</h1>

    <h2>About Me</h2>
    <p>
        I am a BSc AI student interested in Web Development
        and Python Full Stack Development.
    </p>

    <h2>Skills</h2>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
        <li>Python</li>
    </ul>

    <h2>Projects</h2>
    <p>Portfolio Website</p>

    <h2>Contact</h2>
    <p>Email: tejaborukati@gmail.com</p>

</body>
</html>

#style.css
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(to right, #dbeafe, #f0f9ff);
    margin: 0;
    padding: 40px;
    color: #222;
}

h1 {
    color: #1d4ed8;
    text-align: center;
    font-size: 40px;
    margin-bottom: 20px;
}

h2 {
    color: #2563eb;
    border-bottom: 2px solid #93c5fd;
    padding-bottom: 5px;
    margin-top: 30px;
}

p {
    font-size: 18px;
    line-height: 1.6;
}

ul {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    width: fit-content;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

li {
    margin: 10px 0;
    font-size: 17px;
}

body {
    max-width: 800px;
    margin: auto;
}

#js
alert("Welcome to Sai Tejaswi Portfolio Website!");

document.addEventListener("DOMContentLoaded", function () {

    const headings = document.querySelectorAll("h2");

    headings.forEach(function (heading) {

        heading.addEventListener("mouseover", function () {
            heading.style.color = "red";
            heading.style.transition = "0.3s";
        });

        heading.addEventListener("mouseout", function () {
            heading.style.color = "#2563eb";
        });

    });

});
