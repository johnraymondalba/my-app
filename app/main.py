from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>John Raymond S. Alba</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --navy: #0a1628;
      --gold: #c9a84c;
      --gold-light: #e8c97e;
      --cream: #f5f0e8;
      --muted: #8a9bb0;
      --white: #ffffff;
    }

    body {
      background-color: var(--navy);
      color: var(--cream);
      font-family: 'DM Sans', sans-serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      overflow-x: hidden;
    }

    /* Background grid */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(201,168,76,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(201,168,76,0.04) 1px, transparent 1px);
      background-size: 60px 60px;
      pointer-events: none;
    }

    .card {
      background: linear-gradient(145deg, #0f2040, #0a1628);
      border: 1px solid rgba(201,168,76,0.25);
      border-radius: 4px;
      max-width: 720px;
      width: 100%;
      padding: 3.5rem;
      position: relative;
      box-shadow: 0 30px 80px rgba(0,0,0,0.6), inset 0 1px 0 rgba(201,168,76,0.1);
      animation: fadeUp 0.8s ease both;
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* Corner accents */
    .card::before, .card::after {
      content: '';
      position: absolute;
      width: 24px; height: 24px;
      border-color: var(--gold);
      border-style: solid;
    }
    .card::before { top: -1px; left: -1px; border-width: 2px 0 0 2px; }
    .card::after  { bottom: -1px; right: -1px; border-width: 0 2px 2px 0; }

    .badge {
      display: inline-block;
      font-size: 0.68rem;
      font-weight: 500;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--gold);
      border: 1px solid rgba(201,168,76,0.35);
      padding: 0.3rem 0.9rem;
      border-radius: 2px;
      margin-bottom: 1.8rem;
    }

    h1 {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2rem, 5vw, 3.2rem);
      font-weight: 900;
      line-height: 1.1;
      color: var(--white);
      margin-bottom: 0.4rem;
    }

    h1 span { color: var(--gold); }

    .divider {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin: 1.6rem 0;
    }
    .divider::before, .divider::after {
      content: '';
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(201,168,76,0.4), transparent);
    }
    .divider-icon { color: var(--gold); font-size: 0.8rem; }

    .course-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(201,168,76,0.08);
      border: 1px solid rgba(201,168,76,0.2);
      border-radius: 3px;
      padding: 0.6rem 1rem;
      font-size: 0.88rem;
      color: var(--gold-light);
      font-weight: 500;
      margin-bottom: 2rem;
    }
    .course-tag .dot { width: 6px; height: 6px; background: var(--gold); border-radius: 50%; }

    .intro {
      font-size: 1rem;
      line-height: 1.85;
      color: #b8c8d8;
      font-weight: 300;
    }

    .intro strong { color: var(--cream); font-weight: 500; }

    .info-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-top: 2.2rem;
    }

    .info-item {
      background: rgba(255,255,255,0.02);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 3px;
      padding: 1rem 1.2rem;
    }

    .info-label {
      font-size: 0.65rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 0.3rem;
    }

    .info-value {
      font-size: 0.92rem;
      color: var(--cream);
      font-weight: 500;
    }

    .footer {
      margin-top: 2.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid rgba(255,255,255,0.06);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: gap;
      gap: 0.5rem;
    }

    .footer-label {
      font-size: 0.75rem;
      color: var(--muted);
      letter-spacing: 0.05em;
    }

    .footer-course {
      font-size: 0.75rem;
      color: var(--gold);
      font-weight: 500;
      letter-spacing: 0.08em;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">Student Profile</div>

    <h1>John Raymond<br/><span>S. Alba</span></h1>

    <div class="divider"><span class="divider-icon">✦</span></div>

    <div class="course-tag">
      <span class="dot"></span>
      Bachelor of Science in Computer Science
    </div>

    <p class="intro">
      Hello! I am a <strong>3rd year student</strong> at
      <strong>Camarines Sur Polytechnic Colleges</strong>, currently pursuing my
      Bachelor's degree in Computer Science. I am passionate about software
      development and continuously honing my skills through hands-on projects
      and academic coursework. This journey has equipped me with a strong
      foundation in programming, systems thinking, and collaborative problem-solving.
    </p>

    <div class="info-grid">
      <div class="info-item">
        <div class="info-label">Institution</div>
        <div class="info-value">Camarines Sur Polytechnic Colleges</div>
      </div>
      <div class="info-item">
        <div class="info-label">Year Level</div>
        <div class="info-value">3rd Year</div>
      </div>
      <div class="info-item">
        <div class="info-label">Degree Program</div>
        <div class="info-value">BS Computer Science</div>
      </div>
      <div class="info-item">
        <div class="info-label">Status</div>
        <div class="info-value">Active Student</div>
      </div>
    </div>

    <div class="footer">
      <span class="footer-label">Submitted as a Final Learning Task</span>
      <span class="footer-course">Software Engineering 2</span>
    </div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
