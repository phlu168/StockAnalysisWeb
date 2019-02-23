import { Button } from 'antd';
import React from 'react';

class loadingButton extends React.Component{
    state = {
        loading: false,
        iconLoading: false,
    }
    //const contend = this.props.data;
    enterLoading = () => {
      this.setState({ loading: true });
    }
  
    enterIconLoading = () => {
      this.setState({ iconLoading: true });
    }
  
    render() {
      return (
          <Button type="primary" icon="poweroff" loading={this.state.iconLoading} onClick={this.enterIconLoading}>
            Click me!
          </Button>
          
      )}
      
}

export default loadingButton;