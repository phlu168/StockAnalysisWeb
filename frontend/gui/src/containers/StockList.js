import React from 'react';
import Stock from '../components/Stock';
import axios from 'axios';
import {Button} from 'antd';


class StockList extends React.Component{
    // query from api 
    
    state={
        stocks: [],
        loading: false,
        iconLoading: false,

     }
    
    enterLoading = () => {
        this.setState({ loading: true });
      }
    
    enterIconLoading = () => {
        this.setState({ iconLoading: true });
    }
    // ajax why we need cross headers?
    componentDidMount(){
        console.log("getting data");
        axios.get('http://127.0.0.1:8000/stockapi').then(
            res =>{
                this.setState({
                    stocks: res.data
                });
                console.log(res.data);
            }

        )
    }

    updateRequest(){
        axios.post('http://127.0.0.1:8000/stockapi').then(
            res =>{
                res = "update";
                console.log(res);
            }

        )
    }

    render(){
        return(
            //console.log("from sotck retunr data")
            
            <div>
            <Button type="primary" icon="poweroff" loading={this.state.iconLoading} onClick={
                }>
              Update
            </Button>
            <Stock data={this.state.stocks}>
            
            </Stock>
            </div> 
        )
    }

}
export default StockList;