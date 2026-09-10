from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def bmi_checker():
    bmi = None
    category = None
    error = None

    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])

            if weight <= 0 or height <= 0:
                error = 'Please enter positive values for weight and height.'
            else:
                height_m = height / 100
                bmi = round(weight / (height_m ** 2), 2)

                if bmi < 18.5:
                    category = 'Underweight'
                elif bmi < 25:
                    category = 'Normal weight'
                elif bmi < 30:
                    category = 'Overweight'
                else:
                    category = 'Obesity'
        except (ValueError, TypeError):
            error = 'Please enter valid numbers.'

    return render_template('index.html', bmi=bmi, category=category, error=error)


if __name__ == '__main__':
    app.run(debug=True)
