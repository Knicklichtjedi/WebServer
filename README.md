# WebServer
Webserver functionalities with Flask and pandas.

![Example of the web application. It displays a scatter plot where points are organized in the shape of a slightly angled parallelogram.](web_app.png "Example of the web application.")

## Building

1. Install python 3.12
2. Run `python -m pip install -r requirements.txt`
2. Install npm
3. CD to `/frontend`
4. Run `npm install`
5. Create `.env` file in `/frontend` folder and add `VITE_API_BASE_URL=http://127.0.0.1:5000`or with a different url if your server has a different address
5. Run `npm run build`

## Starting
1. Start `WebServer.py`

## Technologies
### Frontend
- Vite 5.0.5
- Vue 3.4.27
- Bootstrap 5.3.3
- Bootstrap-vue-next 0.21.2
- plotly.js 2.33.0

### Backend
- flask 3.0.3
- pandas 2.2.2
- numpy 1.26.4
