import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

const Chart = (props) => {
  const data = props.chartsData;
  return (
    
      <LineChart
        width={1200}
        height={500}
        data={data}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis dataKey='issues'/>
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="issues"
          stroke="#8884d8"
          activeDot={{ r: 8 }}
        />
      </LineChart>
  );
};

export default Chart;
