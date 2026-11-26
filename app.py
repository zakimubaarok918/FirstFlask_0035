from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  pesan_output = None

  if request.method == "POST":
    parameter_teks = request.form.get("nama_input", "").strip()

    if parameter_teks:
      pesan_output = f"Parameter POST diterima: {parameter_teks}"
    else:
      pesan_output = "Parameter kosong. Silakan masukkan teks."

  return render_template("index.html", pesan_output=pesan_output)


if __name__ == "__main__":
  app.run(debug=True)
