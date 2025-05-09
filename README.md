<!DOCTYPE html>
<html lang="en">
<head>
<style type="text/css">
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
}

input {
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  margin-top: 20px;
  padding: 10px;
  background: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
}

.btn:hover {
  background: #0056b3;
}
</style>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FUDMA Recommender - Home</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <h1>Welcome to FUDMA Course Recommender</h1>
    <p>This system will help you find the best course based on your UTME scores and WAEC/NECO subjects.</p>
    <a href="Rec2.html" class="btn">Get Started</a>
  </div>
</body>
<script type="text/javascript">
// UTME Form Submission
document.getElementById('utme-form').addEventListener('submit', function (e) {
  e.preventDefault();
  // Store UTME data in localStorage
  const utmeData = {
    subject1: document.getElementById('subject1').value,
    score1: document.getElementById('score1').value,
    subject2: document.getElementById('subject2').value,
    score2: document.getElementById('score2').value,
    subject3: document.getElementById('subject3').value,
    score3: document.getElementById('score3').value,
    subject4: document.getElementById('subject4').value,
    score4: document.getElementById('score4').value,
  };
  localStorage.setItem('utmeData', JSON.stringify(utmeData));
  window.location.href = 'waec-neco.html';
});

// WAEC/NECO Form Submission
document.getElementById('waec-neco-form').addEventListener('submit', function (e) {
  e.preventDefault();
  // Store WAEC/NECO data in localStorage
  const waecNecoData = {
    subject1: document.getElementById('subject1').value,
    subject2: document.getElementById('subject2').value,
    subject3: document.getElementById('subject3').value,
    subject4: document.getElementById('subject4').value,
    subject5: document.getElementById('subject5').value,
  };
  localStorage.setItem('waecNecoData', JSON.stringify(waecNecoData));
  window.location.href = 'recommendation.html';
});

// Recommendation Logic
window.onload = function () {
  if (window.location.pathname.endsWith('recommendation.html')) {
    const utmeData = JSON.parse(localStorage.getItem('utmeData'));
    const waecNecoData = JSON.parse(localStorage.getItem('waecNecoData'));

    // Example recommendation logic
    let recommendedCourse = 'Computer Science'; // Default recommendation
    if (utmeData.subject1.toLowerCase().includes('math') && waecNecoData.subject1.toLowerCase().includes('math')) {
      recommendedCourse = 'Mathematics';
    } else if (utmeData.subject1.toLowerCase().includes('phy') && waecNecoData.subject1.toLowerCase().includes('phy')) {
      recommendedCourse = 'Physics';
    }

    document.getElementById('recommended-course').textContent = recommendedCourse;
  }
};
</script>
</html>

