import React, { Component } from 'react';
import Plot from "react-plotly.js";

class Plotly extends React.Component {
    constructor(props){
        super(props);
        this.state = {data: []}
    }

    

    // defining backend fetch
    componentDidMount(){
        fetch('http://127.0.0.1:8000/series',)
            .then(response => response.json())
            .then(response => this.setState({'data': response})
            )
    }

    render(){
        return (
            <div>
                <Plot
                
                    data={[
                        {type: 'scatter',
                         mode: 'lines',
                         x : this.state.data.dates,
                         y: this.state.data.values,
                         marker: {color:'blue'}}
                    ]}
                    layout ={{width: 1100 , height: 800, title: 'FRED ECONOMIC DATA'}}
                    />

            </div>
        )
    }
}
export default Plotly;