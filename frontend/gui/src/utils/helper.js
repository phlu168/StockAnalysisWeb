import axios from 'axios';


export default function getDataFromPostgres(stockSymbol){
    const promiseData = axios.get(`http://127.0.0.1:8000/stockapi/price/?sym=${stockSymbol}`).then(
        res =>{
            let values = res.data
            let data = values.map((obj) => {
                let date = obj.date + 'T05:00:00.000Z'
                obj.date = new Date(date)
                return obj
            })
            console.log(data);
            return res;
        }

    ).then(data=>{
        const items = data;
        console.log(data)
        return data;
    })
    console.log(promiseData);
    return promiseData;

}