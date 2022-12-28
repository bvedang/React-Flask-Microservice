import './App.css';
import Navigation from './components/Navigation/Navigation';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Charts/Home';
import AngularCliCharts from './components/Charts/AngularCliCharts';
import AngularMapsCharts from './components/Charts/AngularMaps/AngularMapsCharts';
import D3Charts from './components/Charts/D3Charts';
import FlaskCharts from './components/Charts/FlaskCharts';
import GoCharts from './components/Charts/GoCharts';
import GoGithubCharts from './components/Charts/GoGithubCharts';
import KerasCharts from './components/Charts/KerasCharts';
import MaterialCharts from './components/Charts/MaterialCharts';
import ReactLocalCharts from './components/Charts/ReactlocalCharts';
import TensorflowCharts from './components/Charts/TensorflowCharts';

function App() {
  return (
    <div className="App">
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/angularCli/*" element={<AngularCliCharts />}></Route>
        <Route path="//angularmaps/*" element={<AngularMapsCharts />}></Route>
        <Route path="/d3/*" element={<D3Charts />}></Route>
        <Route path="/flask/*" element={<FlaskCharts />}></Route>
        <Route path="/go/*" element={<GoCharts />}></Route>
        <Route path="/goGithub/*" element={<GoGithubCharts />}></Route>
        <Route path="/keras/*" element={<KerasCharts />}></Route>
        <Route path="/material/*" element={<MaterialCharts />}></Route>
        <Route path="/react/*" element={<ReactLocalCharts />}></Route>
        <Route path="/tensorflow/*" element={<TensorflowCharts />}></Route>
      </Routes>
    </div>
  );
}

export default App;
