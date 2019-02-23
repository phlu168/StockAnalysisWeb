import React from 'react';
import {Route} from 'react-router-dom';
import StockList from './containers/StockList';
import StockDetail from './containers/StockDetail'
//import renderEmpty from 'antd/lib/config-provider/renderEmpty';

const BaseRouter = ()=> (
    <div>
        <Route exact path = '/' component = {StockList} />
        <Route exact path = '/:sym' component = {StockDetail} />
    </div>
)

export default BaseRouter;