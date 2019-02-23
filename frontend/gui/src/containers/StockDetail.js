import React from 'react';
//import Stock from '../components/Stock';
import axios from 'axios';
import {Card} from 'antd';
//for chart
import Chart from './CandleStickChart';
import { TypeChooser } from "react-stockcharts/lib/helper";
import getDataFromPostgres from '../utils/helper';

class StockDetail extends React.Component {

    state={
        loadingData:true, // solve problem of ajax with unmounted component
        stock: {}
    }

    componentDidMount(){
        //this._isMounted = true;
        //console.log(this.props);
        console.log(this.state.stock);
        //this._isMounted = true;
        const stockSymbol = this.props.match.params.sym;
        //console.log(this.props);
        axios.get(`http://127.0.0.1:8000/stockapi/price/?sym=${stockSymbol}`).then(
            res =>{
                let values = res.data
                let data = values.map((obj) => {
                    let date = obj.date + 'T05:00:00.000Z'
                    obj.date = new Date(date)
                    return obj
                })
                this.setState({
                    stock: data,
                    loadingData: false,
                });
                //console.log(res.data);
            }

        );
        console.log(this.state.stock);
    }
	render() {

        if (this.state.loadingData) {
            return <div>Loading...</div>
        }
        return (
            <div>
                
                <TypeChooser>
                    
                    {type => <Chart type={type} data={this.state.stock} />}
                </TypeChooser>

            </div>
        );
      	
	}
}

export default StockDetail;
