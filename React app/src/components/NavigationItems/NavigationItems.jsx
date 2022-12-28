import React from "react";
import './NavigationItems.css'
import { NavLink } from "react-router-dom";

const NavigationItems = (props) =>{
    let cssclass = 'navigationItems'
    if (props.isActive){
        cssclass = "active"
    }
    return (
        <div onClick={props.onClick} className={cssclass}>
            <NavLink></NavLink>
            <li>{props.repoName}</li>
        </div>
    );
}

export default NavigationItems