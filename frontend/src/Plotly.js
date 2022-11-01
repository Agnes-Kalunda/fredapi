import React, { Component } from 'react';
import Plot from "react-plotly.js";

class Plotly extends React.Component {
    constructor(props){
        super(props);
        this.state = {data: []}
    }
    // defining callback url
    
    componentDidMount(){
        fetch('https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key=644cd67ebf8d504be3973f6b815a4ac9&file_type=json')
            .then(response => response.json())
            .then(response => this.setState({'start': response.start}))
    }

    render(){
        return (
            <div>
                <Plot
                
                    data={[
                        {type: 'scatter',
                         mode: 'lines',
                         x : {value},
                         y:{date},
                         marker: {color:'blue'}}
                    ]}
                    layout ={{width: 1100 , height: 800, title: 'hjgvjhkgvhvjfuj'}}
                    />

            </div>
        )
    }
}
export default Plotly;