from flask import Flask, render_template
import os

app = Flask(__name__)

# === ROUTES (HANYA TAMPILKAN HTML) ===
@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/artikel')
def artikel():
    return render_template('artikel.html')

@app.route('/kalori')
def kalori():
    return render_template('kalori.html')
# === RUN APP ===
if __name__ == '__main__':
    # Ubah host jadi '0.0.0.0' agar bisa diakses di jaringan lokal
    app.run(host='0.0.0.0', port=5000, debug=True)