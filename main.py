from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired
from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location_URL = URLField('Cafe Location on Google Maps(URL)', validators=[DataRequired()])
    cafe_open_time = StringField('Opening Time e.g.8AM', validators=[DataRequired()])
    cafe_close_time = StringField('Closing Time e.g.5.30PM', validators=[DataRequired()])
    cafe_rating = SelectField('Coffee Rating', choices = [0,1,2,3,4,5], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices = [0,1,2,3,4,5], validators=[DataRequired()])
    power_rating = SelectField('Power Socket availability', choices = [0,1,2,3,4,5], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow([form.cafe.data, form.Location_URL.data, form.cafe_open_time.data, form.cafe_close_time.data,form.cafe.data, form.cafe_rating.data, form.wifi_rating.data, form.power_rating.data ])

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
