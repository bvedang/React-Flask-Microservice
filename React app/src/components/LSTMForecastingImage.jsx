import React from 'react';
import Typography from '@mui/material/Typography';

function LSTMForecastingImage(props) {
  if (props.url === 'URL_NOTFOUND') {
    return (
      <div>
        <Typography variant="h5" gutterBottom>
          Something went wrong! Unable to generate {props.forecastOf} forecast
        </Typography>
      </div>
    );
  }
  return (
    <div>
      <Typography variant="h5" gutterBottom>
        Forecast of Repo{' ' + props.forecastOf}
      </Typography>
      <img
        src={'http://127.0.0.1:5002/static/' + props.url}
        alt={props.forecastOf}
      />
    </div>
  );
}

export default LSTMForecastingImage;
