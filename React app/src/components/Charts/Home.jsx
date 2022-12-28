import React, { useEffect, useState } from 'react';
import {
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
import './main.css';

const Home = () => {
  const [forks, setForks] = useState({});
  const [stars, setStars] = useState({});
  const [stackedCreatedClosed, setstackedCreatedClosed] = useState({});
  useEffect(() => {
    const url = 'http://127.0.0.1:5000/home';
    const fetchData = async () => {
      try {
        const resp = await fetch(url);
        const data = await resp.json();
        setStars(data.stars);
        setForks(data.forks);
        setstackedCreatedClosed(data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  }, []);
  return (
    <div className="mainComponent">
      <div>
        <Typography variant="h5" gutterBottom>
          Bar Plot of repository Stars
        </Typography>
        <Grid container justifyContent="center" spacing={2}>
          <BarChart
            width={1000}
            height={450}
            data={stars}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis dataKey="starcount" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Bar dataKey="starcount" fill="#413ea0" />
          </BarChart>
        </Grid>
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
        Bar Plot of repository Forks
        </Typography>
        <Grid container justifyContent="center" spacing={2}>
          <BarChart
            width={1000}
            height={450}
            data={forks}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis dataKey="forkcount" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Bar dataKey="forkcount" fill="#413ea0" />
          </BarChart>
        </Grid>
      </div>
      <div>
        <Typography variant="h5" gutterBottom>
          A Stacked Bar Chart to plot the issues closed and created for each   Repository
        </Typography>
        <Grid container justifyContent="center" spacing={2}>
          <BarChart
            width={1000}
            height={450}
            data={stackedCreatedClosed.stackedCreatedClosed}
            margin={{
              top: 20,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="created" stackId="a" fill="#413ea0" />
            <Bar dataKey="closed" stackId="a" fill="#ff7300" />
          </BarChart>
        </Grid>
      </div>
    </div>
  );
};
export default Home;
