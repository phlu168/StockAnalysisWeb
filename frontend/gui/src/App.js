import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';
import BaseRouter from './routes';
import {BrowserRouter as Router} from 'react-router-dom';
import 'antd/dist/antd.css'; 

import CustomLayout from './containers/Layout';
import StockList from './containers/StockList';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <CustomLayout>
            <BaseRouter/>
          </CustomLayout>
         </Router>
        
      </div>
    );
  }
}

export default App;
