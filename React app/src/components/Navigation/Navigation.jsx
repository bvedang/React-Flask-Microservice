import React from 'react';
import './Navigation.css';

import { NavLink } from 'react-router-dom';
import NavigationItems from '../NavigationItems/NavigationItems';
import Home from '../Charts/Home';
import AngularCliCharts from '../Charts/AngularCliCharts';
import AngularMapsCharts from '../Charts/AngularMaps/AngularMapsCharts';
import D3Charts from '../Charts/D3Charts';
import FlaskCharts from '../Charts/FlaskCharts';
import GoCharts from '../Charts/GoCharts';
import GoGithubCharts from '../Charts/GoGithubCharts';
import KerasCharts from '../Charts/KerasCharts';
import MaterialCharts from '../Charts/MaterialCharts';
import ReactLocalCharts from '../Charts/ReactlocalCharts';
import TensorflowCharts from '../Charts/TensorflowCharts';

const Navigation = () => {
  const activeState = {
    go: true,
    goGithub: false,
    material: false,
    angularCLi: false,
    angularMaps: false,
    d3: false,
    reactLocal: false,
    tensorflow: false,
    keras: false,
    flask: false,
  };
  const activateNavigation = (navkey) => {
    for (const key in activeState) {
      if (key === navkey) {
        continue;
      } else {
        activeState[key] = false;
      }
    }
    activeState[navkey] = true;
  };
  return (
    <div className="navigation">
      <div>
        <NavLink className={'navigationItems'} to="/">
          Home
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/angularCli">
          AngularCli
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/angularmaps">
          AngularMaps
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/d3">
          D3
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/flask">
          Flask
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/react">
          React
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/go">
          Go
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/goGithub">
          GoGithub
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/keras">
          Keras
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/material">
          Material
        </NavLink>
      </div>
      <div>
        <NavLink className={'navigationItems'} to="/tensorflow">
          Tensorflow
        </NavLink>
      </div>
    </div>
  );
};

export default Navigation;
