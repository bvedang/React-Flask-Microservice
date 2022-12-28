import React, { useEffect, useState } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  BarChart,
  Bar,
} from 'recharts';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import '../main.css';

const AngularMapsCharts = () => {
  const [createdMonth, setCreatedMonth] = useState({});
  const [closedIssueWeekly, setClosedIssueWeekly] = useState({});
  const [createdIssues, setCreatedIssues] = useState({});
  const [fbIssueforecast, setfbIssueforecast] = useState('');
  const [fbclosedforecast, setfbClosedforecast] = useState('');
  const [fbforecastCommit, setfbforecastCommit] = useState('');
  const [fbforecastpull, setfbforecastpull] = useState('');
  const [fbforecastrelease, setfbforecastrelease] = useState('');

  useEffect(() => {
    const url = 'http://127.0.0.1:5000/angular-google-maps';
    const fetchData = async () => {
      try {
        const resp = await fetch(url);
        const data = await resp.json();
        setCreatedMonth(data.createdMonth);
        setClosedIssueWeekly(data.closedWeekly);
        setCreatedIssues(data.issues);
        setfbClosedforecast(data.fbforecastclosedurl);
        setfbIssueforecast(data.fbforecastissueurl);
        setfbforecastCommit(data.fbforecastCommit);
        setfbforecastpull(data.fbforecastpull);
        setfbforecastrelease(data.fbforecastrelease);
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  }, []);
  const pullImage = () => {
    if (fbforecastpull === 'No pull Information found') {
      return (
        <div>
          <Typography variant="h5" gutterBottom>
            Something went wrong! Unable to generate pull forecast
          </Typography>
        </div>
      );
    }
    return (
      <img src={'http://127.0.0.1:5000/static/' + fbforecastpull} alt="" />
    );
  };
  const releaseImage = () => {
    if (fbforecastrelease === 'No pull Information found') {
      return (
        <div>
          <Typography variant="h5" gutterBottom>
            Something went wrong! Unable to generate pull forecast
          </Typography>
        </div>
      );
    }
    return (
      <img src={'http://127.0.0.1:5000/static/' + fbforecastrelease} alt="" />
    );
  };
  const commitImage = () => {
    if (fbforecastCommit === 'No pull Information found') {
      return (
        <div>
          <Typography variant="h5" gutterBottom>
            Something went wrong! Unable to generate pull forecast
          </Typography>
        </div>
      );
    }
    return (
      <img src={'http://127.0.0.1:5000/static/' + fbforecastCommit} alt="" />
    );
  };
  return (
    <div className="mainComponent">
      <div className="grpahDiv">
        <Typography variant="h5" gutterBottom>
          A Line Chart to plot the issues for Sebholstein/Angular-Google-Maps
          Repository
        </Typography>
        <Grid container justifyContent="center" spacing={2}>
          <LineChart width={1000} height={450} data={createdIssues}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="created_at" />
            <YAxis dataKey="issue_number" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Line
              type="monotone"
              dataKey="issue_number"
              stroke="#413ea0"
              activeDot={{ r: 8 }}
            />
          </LineChart>
        </Grid>
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          A Bar Chart to plot the issues created for every month for
          Sebholstein/Angular-Google-Maps Repository
        </Typography>
        <Grid container justifyContent="center" spacing={2}>
          <BarChart
            width={1000}
            height={450}
            data={createdMonth}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis dataKey="issues" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Bar dataKey="issues" fill="#413ea0" />
          </BarChart>
        </Grid>
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          A Bar Chart to plot the issues closed for every Week for
          Sebholstein/Angular-Google-Maps Repository
        </Typography>
        <Grid container justifyContent="center" spacing={2}>
          <BarChart
            width={1000}
            height={450}
            data={closedIssueWeekly}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis dataKey="issues" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Bar dataKey="issues" fill="#413ea0" />
          </BarChart>
        </Grid>
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          FB Prophet Issue Forecast
        </Typography>
        <img src={'http://127.0.0.1:5000/static/' + fbIssueforecast} alt="" />
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          FB Prophet Closed Issue Forecast
        </Typography>
        <img src={'http://127.0.0.1:5000/static/' + fbclosedforecast} alt="" />
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          FB Prophet Commit Forecast
        </Typography>
        {commitImage()}
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          FB Prophet Pulls Forecast
        </Typography>
        {pullImage()}
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          FB Prophet Release Forecast
        </Typography>
        {releaseImage()}
      </div>
    </div>
  );
};

export default AngularMapsCharts;
