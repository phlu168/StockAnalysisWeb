import React from 'react';
import { List, Avatar, Icon } from 'antd';

const IconText = ({ type, text }) => (
  <span>
    <Icon type={type} style={{ marginRight: 8 }} />
    {text}
  </span>
);

const Stock = (props) => {
    
    console.log("from sotck return data");
    return(
        <List
            itemLayout="vertical"
            size="large"
            pagination={{
            onChange: (page) => {
                console.log(page);
            },
            pageSize: 3,
            }}
            dataSource={props.data}
            footer={<div><b>ant design</b> footer part</div>}
            renderItem={item => (
            <List.Item
                key={item.title}
                actions={[<IconText type="star-o" text="156" />, <IconText type="like-o" text="156" />, <IconText type="message" text="2" />]}
                extra={<img width={272} alt="logo" src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png" />}
            >
            
            {console.log("item "+item)}
           
            <List.Item.Meta
            avatar={<Avatar src={item.avatar} />}
            title={<a href={`/${item.symbol}`}>{item.symbol}</a>}
            description={
                <div>
                   <b>{item.startDate+" "+item.endDate+"!"}</b>     
                </div>
                //{repeat(i)} <b>{item.startDate+" "+item.endDate+"!"}</b>
            }
            />
            </List.Item>
            )}
        />
    )
}

export default Stock;



