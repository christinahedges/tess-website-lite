from flask import Flask, render_template
import io
import base64
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
from datetime import date, datetime

from helper_codes import find_tess_today as find_tess_today
from helper_codes import plot_tess_today as plot_tess_today

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():

    today = str(date.today())
    today_split = datetime.strptime(today, "%Y-%m-%d")
    today_decimal = today_split.year + (today_split.timetuple().tm_yday - 1) / 365.2425

    sector_, orbit_ = find_tess_today(today_decimal)
    aa = plot_tess_today(sector_, orbit_)

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == '__main__':
    app.run(debug=True)