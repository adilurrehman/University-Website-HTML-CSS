import os

css = """/* Modern, Professional, Beginner-friendly University CSS */
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
}

body {
    background-color: #f4f6f8;
    color: #333;
    line-height: 1.6;
}

/* Header & Navigation */
.header {
    background-color: #003366; /* Navy Blue */
    color: #fff;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 5%;
    max-width: 1400px;
    margin: auto;
}

.navbar img {
    height: 60px;
    background: #fff;
    border-radius: 5px;
    padding: 5px;
}

.nav-links ul {
    list-style: none;
    display: flex;
}

.nav-links ul li {
    padding: 10px 15px;
}

.nav-links ul li a {
    color: #fff;
    text-decoration: none;
    font-size: 16px;
    font-weight: 600;
    text-transform: uppercase;
    transition: color 0.3s ease;
}

.nav-links ul li a:hover {
    color: #fca311; /* Gold accent */
}

/* Page Hero Header */
.subheader {
    background-image: linear-gradient(rgba(0,51,102,0.8), rgba(0,51,102,0.8)), url('campus.jpg');
    background-size: cover;
    background-position: center;
    color: #fca311;
    text-align: center;
    padding: 80px 20px;
}

.subheader h1 {
    font-size: 48px;
    color: #fff;
    margin-bottom: 20px;
}

.butt {
    display: inline-block;
    background-color: #fca311;
    color: #003366;
    padding: 10px 25px;
    text-decoration: none;
    font-weight: bold;
    border-radius: 5px;
    transition: background 0.3s ease;
}
.butt:hover {
    background-color: #e08e0b;
}

/* Main Section Wrapper */
section {
    padding: 60px 5%;
    max-width: 1400px;
    margin: auto;
}

.section-title {
    text-align: center;
    font-size: 36px;
    color: #003366;
    margin-bottom: 40px;
}

/* Cards Grid Layout */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.card {
    background: #fff;
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

.card h3 {
    color: #003366;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    background-color: #002244;
    color: #ccc;
    text-align: center;
    padding: 40px 20px;
    margin-top: 50px;
}

.footer h4 {
    color: #fff;
    font-size: 24px;
    margin-bottom: 15px;
}

.footer .social-icons i {
    font-size: 20px;
    color: #fca311;
    margin: 0 10px;
    cursor: pointer;
}

.footer p {
    margin-top: 15px;
    font-size: 14px;
}

/* Forms */
.form-container {
    max-width: 600px;
    margin: auto;
    background: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: 600;
    color: #003366;
}

.form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.btn-submit {
    background-color: #003366;
    color: #fff;
    padding: 12px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    width: 100%;
}
.btn-submit:hover {
    background-color: #002244;
}

/* Map/Location */
.location iframe {
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* Table */
.data-table {
    width: 100%;
    border-collapse: collapse;
    background: #fff;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.data-table th, .data-table td {
    padding: 15px;
    border: 1px solid #ddd;
    text-align: left;
}
.data-table th {
    background: #003366;
    color: #fff;
}
"""

def generate_header(title):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AKz University - {title}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <a href="index.html" style="color:#fff; text-decoration: none; font-size: 24px; font-weight: bold;">
                <i class="fa fa-graduation-cap"></i> AKz University
            </a>
            <div class="nav-links">
               <ul>
                   <li><a href="index.html">HOME</a></li>
                   <li><a href="About.html">ABOUT</a></li>
                   <li><a href="courses.html">COURSES</a></li>
                   <li><a href="faculty2.html">FACULTY</a></li>
                   <li><a href="register.html">REGISTER</a></li>
                   <li><a href="contact.html">CONTACT</a></li>
               </ul>
            </div>    
        </nav>
    </header>
'''

footer = '''
    <footer class="footer">
        <h4>AKz University</h4>
        <div class="social-icons">
            <i class="fa-solid fa-building-columns"></i>
            <i class="fa-solid fa-phone"></i>
            <i class="fa-solid fa-envelope"></i>
        </div>
        <p>A beacon of academic excellence, fostering innovation and knowledge in the realm of engineering and technology.<br>&copy; 2026 AKz University. All rights reserved.</p>
    </footer>
</body>
</html>
'''

files = {
    'styles.css': css,
    'index.html': generate_header('Home') + '''
    <div class="subheader">
        <h1>Welcome to AKz University</h1>
        <p style="color: white; font-size: 18px; max-width: 800px; margin: auto; margin-bottom: 20px;">
            A premier institution for engineering, technology, and visionary leaders.
        </p>
        <a href="About.html" class="butt">Learn More About Us</a>
    </div>

    <section>
        <h2 class="section-title">Our Departments</h2>
        <div class="grid-container">
            <div class="card">
                <h3>Computer Science</h3>
                <p>Equipping students with modern computing and problem-solving skills for the fast-paced IT industry.</p>
            </div>
            <div class="card">
                <h3>Mechanical Engineering</h3>
                <p>Conceive, design, develop, and test out-of-the-box physical systems and thermal devices.</p>
            </div>
            <div class="card">
                <h3>Electrical Engineering</h3>
                <p>One of our premier programs, featuring state-of-the-art lab facilities and experienced faculty.</p>
            </div>
            <div class="card">
                <h3>Industrial & Manufacturing</h3>
                <p>Learn specialized technical skills specific to the modern manufacturing industry and engineering organizations.</p>
            </div>
        </div>
    </section>

    <section style="background: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); padding: 40px; margin-bottom: 40px;">
        <h2 class="section-title">World-Class Facilities</h2>
        <div class="grid-container">
            <div>
                <h3 style="color:#003366;">Sports Grounds</h3>
                <p>Expansive facilities for outdoor and indoor games including cricket, hockey, tennis, and basketball.</p>
            </div>
            <div>
                <h3 style="color:#003366;">Digital Library</h3>
                <p>Fully searchable web catalog with a huge holding capacity and a reading hall.</p>
            </div>
            <div>
                <h3 style="color:#003366;">Campus Life</h3>
                <p>Beautiful environments designed to foster student collaboration, creativity, and peaceful reflection.</p>
            </div>
        </div>
    </section>
''' + footer,

    'About.html': generate_header('About') + '''
    <div class="subheader">
        <h1>About AKz University</h1>
        <p style="color: #fff; max-width: 700px; margin: auto;">Discover our history, mission, and the community that makes us unique.</p>
    </div>
    
    <section>
        <h2 class="section-title">Our Story</h2>
        <div style="background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-size: 18px;">
            <p style="margin-bottom: 15px;">AKz University was founded with the aim of playing an important role in fulfilling the demand for skilled professionals.</p>
            <p style="margin-bottom: 15px;">Situated at the hub of the engineering industries, the campus is surrounded by lush agricultural land, providing a serene environment for rigorous academic pursuits.</p>
            <p>Our commitment to progressive and innovative outlooks allows our students to grow as modern visionaries contributing to research and development globally.</p>
            <br>
            <a href="courses.html" class="butt">Explore Our Courses</a>
        </div>
    </section>
''' + footer,

    'courses.html': generate_header('Courses') + '''
    <div class="subheader">
        <h1>Academic Programs</h1>
        <p style="color: #fff;">Undergraduate and postgraduate degrees built for the future.</p>
    </div>

    <section>
        <h2 class="section-title">Courses We Offer</h2>
        <div class="grid-container">
            <div class="card">
                <h3>BS Computer Science</h3>
                <p>Accredited by NCEAC. Delivers core concepts in computing.</p>
            </div>
            <div class="card">
                <h3>BS Mechanical Engineering</h3>
                <p>Learn the principles of communication, science, and the physics of machinery.</p>
            </div>
            <div class="card">
                <h3>BS Electrical Engineering</h3>
                <p>Accredited by PEC, an esteemed 4-year undergraduate program.</p>
            </div>
            <div class="card">
                <h3>BS Industrial & Mfg</h3>
                <p>Following modern OBE systems, preparing engineers for industrial transitions.</p>
            </div>
        </div>
    </section>
''' + footer,

    'faculty2.html': generate_header('Faculty') + '''
    <div class="subheader">
        <h1>Meet Our Faculty</h1>
        <p style="color: #fff;">Learn from experienced professionals and researchers.</p>
    </div>

    <section>
        <h2 class="section-title">Department of Computer Science</h2>
        <table class="data-table">
            <thead>
                <tr>
                    <th>Name / Role</th>
                    <th>Qualifications</th>
                    <th>Contact</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Engr. Dr. Abdul Jaleel</b><br>Chairman</td>
                    <td>PhD CS, MSc CS, BSc Engineering</td>
                    <td>abduljaleel@uet.edu.pk</td>
                </tr>
                <tr>
                    <td><b>Engr. Dr. Tayybah Kiren</b><br>Assistant Professor</td>
                    <td>PhD CS, MSc CS</td>
                    <td>tayybah.sahi@gmail.com</td>
                </tr>
                <tr>
                    <td><b>Syed Muhammad Mehdi</b><br>Lecturer</td>
                    <td>PhD (In Progress), MS CS</td>
                    <td>m.mehdi@uet.edu.pk</td>
                </tr>
                <!-- More faculty can be added here easily -->
            </tbody>
        </table>
    </section>
''' + footer,

    'register.html': generate_header('Register') + '''
    <div class="subheader">
        <h1>Admissions Registration</h1>
        <p style="color: #fff;">Take the first step toward a bright future.</p>
    </div>

    <section>
        <div class="form-container">
            <h2 style="color: #003366; text-align: center; margin-bottom: 20px;">Registration Form</h2>
            <form action="#">
                <div class="form-group">
                    <label>Full Name:</label>
                    <input type="text" class="form-control" placeholder="Enter your full name" required>
                </div>
                <div class="form-group">
                    <label>Email Address:</label>
                    <input type="email" class="form-control" placeholder="example@domain.com" required>
                </div>
                <div class="form-group">
                    <label>Program of Interest:</label>
                    <select class="form-control" required>
                        <option value="">Select a Program</option>
                        <option value="cs">Computer Science</option>
                        <option value="me">Mechanical Engineering</option>
                        <option value="ee">Electrical Engineering</option>
                        <option value="ime">Industrial Engineering</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Gender:</label>
                    <div style="display: flex; gap: 15px;">
                        <label style="font-weight: normal;"><input type="radio" name="gender" value="Male"> Male</label>
                        <label style="font-weight: normal;"><input type="radio" name="gender" value="Female"> Female</label>
                    </div>
                </div>
                <button type="submit" class="btn-submit">Submit Registration</button>
            </form>
        </div>
    </section>
''' + footer,

    'contact.html': generate_header('Contact') + '''
    <div class="subheader">
        <h1>Contact Us</h1>
        <p style="color: #fff;">Reach out to us for any queries or admissions help.</p>
    </div>

    <section>
        <h2 class="section-title">Get In Touch</h2>
        <div class="grid-container">
            <div class="card">
                <h3><i class="fa fa-map-marker-alt"></i> Location</h3>
                <p>7km G.T Road, Joura Sian<br>Gukkhar, Punjab, Pakistan</p>
            </div>
            <div class="card">
                <h3><i class="fa fa-phone"></i> Phone</h3>
                <p>+92 55 6770168<br>Mon-Sat, 8am - 4pm</p>
            </div>
            <div class="card">
                <h3><i class="fa fa-envelope"></i> Email</h3>
                <p>admin.uet@uet.edu.pk</p>
            </div>
        </div>
    </section>
    
    <section class="location" style="padding-top:0;">
        <h2 class="section-title">Find Us on the Map</h2>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3370.167745792945!2d74.20527577473466!3d32.361045305129494!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391f20a3705c30c1%3A0x858cebbad07e640!2sUniversity%20of%20Engineering%20%26%20Technology%20Gujranwala%20Campus!5e0!3m2!1sen!2s!4v1703212474442!5m2!1sen!2s" 
        height="450" allowfullscreen="" loading="lazy"></iframe>
    </section>
''' + footer
}

for filename, content in files.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

